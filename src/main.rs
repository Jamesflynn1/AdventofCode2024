mod challenges;


use csv::Reader;
use std::collections::HashMap;
use std::error::Error;
use std::fs::{self, File};
use std::path::Path;
use std::ptr::null;



fn load_days_data(
    data_folder: &str,
    day: &str,
) -> Result<HashMap<String, Reader<File>>, Box<dyn Error>> {
    // Construct the folder path for the day
    let folder_path = format!("{}/{}", data_folder, day);
    println!("Reading the day's data from: {}", folder_path);

    // Create a HashMap to store file name to reader mapping
    let mut readers = HashMap::new();

    // Read the directory entries
    for entry in fs::read_dir(&folder_path)? {
        let entry = entry?;
        let path = entry.path();

        // Check if the entry is a file and has a .csv extension
        if path.is_file() && path.extension().and_then(|s| s.to_str()) == Some("csv") {
            // Get the file name as a String
            if let Some(file_name) = path.file_name().and_then(|s| s.to_str()) {
                // Open the file and create a CSV reader
                let file = File::open(&path)?;
                let rdr = Reader::from_reader(file);

                // Insert into the HashMap
                readers.insert(file_name.to_string(), rdr);
                println!("Found file: {} for {}", file_name, day);
            }
        }
    }

    Ok(readers)
}

fn main() -> Result<(), Box<dyn Error>> {
    let data_folder = "C:\\Users\\james\\Documents\\AdventOfCode2024\\AdventofCode2024\\data";
    let day = "day1";

    // Load CSV readers
    let readers = load_days_data(data_folder, day)?;

    match day  {
        "day1" => challenges::day1::run(&readers)?,
        _ =>  challenges::day1::run(&readers)?,
    };
    // Lookup and execute the challenge for the given day

    Ok(())
}