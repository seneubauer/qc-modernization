using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using CsvHelper;
using System.Globalization;

namespace sw_api
{
	// define the data object
	public class fixture_clearance
	{
		public string? id { get; set; }
		public double py { get; set; }
		public double px { get; set; }
		public double ny { get; set; }
		public double nx { get; set; }
	}

	// define the macro class
	public class sw_macro
	{
		static fixture_clearance get_fixture_clearance(string file_path, string file_name, ref SldWorks app)
		{
			// define the null object
			fixture_clearance null_object = new fixture_clearance
			{
				id = file_name,
				py = 0,
				px = 0,
				ny = 0,
				nx = 0
			};

			// return nothing if the file doesn't exist
			if (!File.Exists(file_path))
				return null_object;
			
			// open the fixture part
			int errors = 0;
			int warnings = 0;
			PartDoc sw_part = (PartDoc)app.OpenDoc6(file_path, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

			// extract the sensor features
			try
			{
				Feature py_feature = (Feature)sw_part.FeatureByName("py");
				Feature px_feature = (Feature)sw_part.FeatureByName("px");
				Feature ny_feature = (Feature)sw_part.FeatureByName("ny");
				Feature nx_feature = (Feature)sw_part.FeatureByName("nx");

				bool e0 = false;
				bool e1 = false;
				bool e2 = false;
				bool e3 = false;
				if (py_feature == null)
					e0 = true;
				if (px_feature == null)
					e1 = true;
				if (ny_feature == null)
					e2 = true;
				if (nx_feature == null)
					e3 = true;
				if (e0 && e1 && e2 && e3)
					return null_object;

				// extract the sensors from their features
				Sensor? py = null;
				Sensor? px = null;
				Sensor? ny = null;
				Sensor? nx = null;
				if (py_feature != null) { py = (Sensor)py_feature.GetSpecificFeature2(); }
				if (px_feature != null) { px = (Sensor)px_feature.GetSpecificFeature2(); }
				if (ny_feature != null) { ny = (Sensor)ny_feature.GetSpecificFeature2(); }
				if (nx_feature != null) { nx = (Sensor)nx_feature.GetSpecificFeature2(); }
				
				// extract the sensor data
				DimensionSensorData? py_data = null;
				DimensionSensorData? px_data = null;
				DimensionSensorData? ny_data = null;
				DimensionSensorData? nx_data = null;
				if (py != null) { py_data = (DimensionSensorData)py.GetSensorFeatureData(); }
				if (px != null) { px_data = (DimensionSensorData)px.GetSensorFeatureData(); }
				if (ny != null) { ny_data = (DimensionSensorData)ny.GetSensorFeatureData(); }
				if (nx != null) { nx_data = (DimensionSensorData)nx.GetSensorFeatureData(); }

				// create the output object
				if (py_data != null && px_data != null && ny_data != null && nx_data != null)
				{
					fixture_clearance output = new fixture_clearance
					{
						id = file_name,
						py = py_data.SensorValue * 1000,
						px = px_data.SensorValue * 1000,
						ny = ny_data.SensorValue * 1000,
						nx = nx_data.SensorValue * 1000
					};

					// release the resources
					app.CloseDoc(file_name + ".sldprt");

					// return the results
					return output;
				}
				else
				{
					// release the resources
					app.CloseDoc(file_name + ".sldprt");

					// return the null result
					return null_object;
				}
			}
			catch (NullReferenceException e)
			{
				// print the error message
				Console.WriteLine($"{file_name}: {e.Message}");

				// release the resources
				app.CloseDoc(file_name + ".sldprt");

				// return null results
				return null_object;
			}
		}

		// define logic loop
		static void Main(string[] args)
		{
			// interpret the initial arguments
			string root_dir = args[0];
			string path_dir = args[1];
			string output_dir = args[2];

			// initialize the solidworks application
			Type? app_type = Type.GetTypeFromProgID("SldWorks.Application.30");
			SldWorks? app = null;
			if (app_type != null) { app = (SldWorks?)Activator.CreateInstance(app_type); }

			// only run the rest of the script if the solidworks application was properly started
			if (app != null)
			{
				List<fixture_clearance> data = new List<fixture_clearance>();
				string[] fixture_folders = Directory.GetDirectories(root_dir);
				foreach (var dir in fixture_folders)
				{
					FileAttributes attr = File.GetAttributes(dir);
					if (attr.HasFlag(FileAttributes.Directory))
					{
						var file_names = Directory.GetFiles(dir).Where(name => name.ToLower().EndsWith(".lnk")).Where(name => !name.Contains("-")).ToList();
						if (file_names.Count > 0)
						{
							var file_name = Path.GetFileName(file_names[0]).Split(".")[0];
							var file_path = Path.Join(path_dir, file_name, file_name + ".sldprt");
							data.Add(get_fixture_clearance(file_path, file_name, ref app));
							Console.WriteLine($"{file_name}");
						}
					}
				}

				// close the solidworks application
				app.CloseAllDocuments(true);
				app.ExitApp();
				
				// write the list of fixture clearances to a csv
				using (var sw = new StreamWriter(output_dir))
				{
					using (var csv = new CsvWriter(sw, CultureInfo.InvariantCulture))
					{
						csv.WriteHeader<fixture_clearance>();
						csv.NextRecord();
						foreach (var record in data)
						{
							csv.WriteRecord(record);
							csv.NextRecord();
						}
					}
				}

				// signal program end
				Console.WriteLine("End of program.");
			}
			else
			{
				Console.WriteLine("Solidworks application initiated as null.");
			}
		}
	}
}