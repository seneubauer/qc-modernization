using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using CsvHelper;
using System.Globalization;

namespace sw_api
{
	// define the data objects
	public class fixture
	{
		public string? id { get; set; }
		public double py { get; set; }
		public double px { get; set; }
		public double ny { get; set; }
		public double nx { get; set; }
		public string? developer_notes { get; set; }
		public string? operator_notes { get; set; }
		public string? anchor_dir { get; set; }
		public double anchor_val { get; set; }
	}

	public class part
	{
		public string? id { get; set; }
		public double py { get; set; }
		public double px { get; set; }
		public double ny { get; set; }
		public double nx { get; set; }
		public string? revision { get; set; }
		public string? developer_notes { get; set; }
		public string? operator_notes { get; set; }
	}

	// define the macro class
	public class sw_macro
	{
		static Dictionary<string, int> NegativeMap = new Dictionary<string, int>();

		static fixture get_sensor_values_fixture(string file_path, string file_name, string sensor_type, ref SldWorks app)
		{
			// define the null object
			fixture null_object = new fixture
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
				Feature py_feature = (Feature)sw_part.FeatureByName($"py{sensor_type}");
				Feature px_feature = (Feature)sw_part.FeatureByName($"px{sensor_type}");
				Feature ny_feature = (Feature)sw_part.FeatureByName($"ny{sensor_type}");
				Feature nx_feature = (Feature)sw_part.FeatureByName($"nx{sensor_type}");

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

				// get the anchor metric
				Feature sw_comments_feature = (Feature)sw_part.FeatureByName("Comments");
				CommentFolder sw_comment_folder = (CommentFolder)sw_comments_feature.GetSpecificFeature2();
				object[] sw_comments = (object[])sw_comment_folder.GetComments();
				string raw_comment = ((Comment)sw_comments[0]).Text;
				string[] comment_split = raw_comment.Split(",");
				string anchor_dir = comment_split[0];
				double anchor_val = double.Parse(comment_split[1]);

				// create the output object
				if (py_data != null && px_data != null && ny_data != null && nx_data != null)
				{
					fixture output = new fixture
					{
						id = file_name,
						py = py_data.SensorValue * 1000,
						px = px_data.SensorValue * 1000,
						ny = ny_data.SensorValue * 1000,
						nx = nx_data.SensorValue * 1000,
						anchor_dir = anchor_dir,
						anchor_val = anchor_val
					};

					// release the resources
					app.CloseAllDocuments(true);

					// return the results
					return output;
				}
				else
				{
					// release the resources
					app.CloseAllDocuments(true);

					// return the null result
					return null_object;
				}
			}
			catch (NullReferenceException e)
			{
				// print the error message
				Console.WriteLine($"{file_name}: {e.Message}");

				// release the resources
				app.CloseAllDocuments(true);

				// return null results
				return null_object;
			}
		}

		static part get_sensor_values_part(string file_path, string file_name, string sensor_type, string id, Dictionary<string, int> mapper, ref SldWorks app)
		{
			// define the null object
			part null_object = new part
			{
				id = id,
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
			AssemblyDoc sw_asm = (AssemblyDoc)app.OpenDoc6(file_path, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

			// extract the sensor features
			try
			{
				Feature py_feature = (Feature)sw_asm.FeatureByName($"py{sensor_type}");
				Feature px_feature = (Feature)sw_asm.FeatureByName($"px{sensor_type}");
				Feature ny_feature = (Feature)sw_asm.FeatureByName($"ny{sensor_type}");
				Feature nx_feature = (Feature)sw_asm.FeatureByName($"nx{sensor_type}");

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

				// extract the revision
				object[] sw_components = (object[])sw_asm.GetComponents(true);
				string? revision = "";
				foreach (var obj in sw_components)
				{
					Component2 sw_component = (Component2)obj;
					if (sw_component.Name2.Contains("_"))
					{
						revision = sw_component.Name2.Split("_").Last().Trim().Split("-").First();
						break;
					}
				}

				// create the output object
				if (py_data != null && px_data != null && ny_data != null && nx_data != null)
				{
					part output = new part
					{
						id = id,
						revision = revision,
						py = py_data.SensorValue * 1000 * mapper[py_data.GetDisplayDimension().GetLowerText()],
						px = px_data.SensorValue * 1000 * mapper[px_data.GetDisplayDimension().GetLowerText()],
						ny = ny_data.SensorValue * 1000 * mapper[ny_data.GetDisplayDimension().GetLowerText()],
						nx = nx_data.SensorValue * 1000 * mapper[nx_data.GetDisplayDimension().GetLowerText()]
					};

					// release the resources
					app.CloseAllDocuments(true);

					// return the results
					return output;
				}
				else
				{
					// release the resources
					app.CloseAllDocuments(true);

					// return the null result
					return null_object;
				}
			}
			catch (NullReferenceException e)
			{
				// print the error message
				Console.WriteLine($"{file_name}: {e.Message}");

				// release the resources
				app.CloseAllDocuments(true);

				// return null results
				return null_object;
			}
		}

		// define logic loop
		static void Main(string[] args)
		{
			// define the negative map dictionary
			NegativeMap.Add("n", -1);
			NegativeMap.Add("", 1);

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
				// get a list of the assembly clearances
				List<part> part_data = new List<part>();
				string[] assembly_folders = Directory.GetDirectories(Path.Join(root_dir, "Parts"));
				foreach (var dir in assembly_folders)
				{
					// get the part number
					string? last_path_segment = dir.Split(new string[] { $"{Path.DirectorySeparatorChar}" }, StringSplitOptions.RemoveEmptyEntries).LastOrDefault();

					// check if a 'Part-Fixture Assembly.sldasm' file exists in this folder
					string file_name = "Part-Fixture Assembly";
					string file_path = Path.Join(dir, file_name + ".sldasm");
					if (File.Exists(file_path) && last_path_segment != null)
					{
						part_data.Add(get_sensor_values_part(file_path, file_name, "_asm", last_path_segment, NegativeMap, ref app));
						Console.WriteLine($"Part: {last_path_segment}");
					}
				}

				// get a list of the fixture clearances
				List<fixture> fixture_data = new List<fixture>();
				string[] fixture_folders = Directory.GetDirectories(Path.Join(root_dir, "Fixtures"));
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
							fixture_data.Add(get_sensor_values_fixture(file_path, file_name, "", ref app));
							Console.WriteLine($"Fixture: {file_name}");
						}
					}
				}

				// close the solidworks application
				app.CloseAllDocuments(true);
				app.ExitApp();

				// write the list of part clearances to a csv
				using (var sw = new StreamWriter(Path.Join(output_dir, "part_data.csv")))
				{
					using (var csv = new CsvWriter(sw, CultureInfo.InvariantCulture))
					{
						csv.WriteHeader<part>();
						csv.NextRecord();
						foreach (var record in part_data)
						{
							csv.WriteRecord(record);
							csv.NextRecord();
						}
					}
				}

				// write the list of fixture clearances to a csv
				using (var sw = new StreamWriter(Path.Join(output_dir, "fixture_data.csv")))
				{
					using (var csv = new CsvWriter(sw, CultureInfo.InvariantCulture))
					{
						csv.WriteHeader<fixture>();
						csv.NextRecord();
						foreach (var record in fixture_data)
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