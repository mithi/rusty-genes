extern crate citydna;
use citydna::city;
// use citydna::examples;
use citydna::{City, Simulation};
use citydna::helper;
use std::process;
use std::env;

fn main() {

    // examples::example_one();
    // examples::example_two();

    // ----------------------
    // PARSE ARGUMENTS
    // ----------------------
    let mut args = env::args().skip(1);

    let specs_filename = args.next()
        .unwrap_or_else( || {
            eprintln!("Please specify filename with simulation specifications. \
            \n USAGE: cargo run ./specs.csv /cities.csv > output.csv");
            process::exit(1)
            }
        );

    let city_filename = args.next()
        .unwrap_or_else( || {
            eprintln!("Please specify filename  with cities. \
            \n USAGE: cargo run ./specs.csv /cities.csv > output.csv");
            process::exit(1)
            }
        );


    // ----------------------
    // EXTRACT SPECS AND DATA
    // ----------------------
    let contents = helper::read_file(&specs_filename);
    let (debug_level, 
         skip,
         iterations, 
         population_size,
         crossover_probability,
         mutation_probability) = helper::parse_specs(&contents).unwrap_or_else(|err| {
            eprintln!("{}", err);
            process::exit(1);
         });

    let contents = helper::read_file(&city_filename);
    let cities: Vec<City> = city::string_to_cities(&contents);
    

    // ----------------------
    // RUN SIMULATION
    // ----------------------

    let mut sim = Simulation::new(
        iterations,
        crossover_probability, 
        mutation_probability, 
        population_size,
        cities
    );

    sim.run(debug_level, skip);
}
