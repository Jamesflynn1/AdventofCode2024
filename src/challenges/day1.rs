use std::fs::File;
use std::collections::HashMap;
use csv::{Error, Reader};


pub fn run(readers: &HashMap<String, Reader<File>>) -> Result<(), Box<dyn std::error::Error>> {
    // Example: Print the names of all files being processed
    //let mut csv = readers.get("day1.csv");
    
    if let Some(csv) = readers.get("day1.csv"){
        for record in csv.records() {
            match record {
                Ok(row) => {
                    println!("Found file: {:?}", row);
                }
                Err(err) => {
                    eprintln!("Error reading record: {}", err);
                    return Err(Box::new(err));
                }
            }
        }
    } else {
        eprintln!("No CSV reader found for day1.csv");
    }

    Ok(())
}