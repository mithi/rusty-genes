use rand::{thread_rng, Rng};
use std::fmt::Debug;
use std::process;
use std::fs::File;
use std::io::prelude::*;

pub fn print_vec<T: Debug>(v: &[T]) {
    for i in v.iter() { println!("{:?}", i); }   
}


pub fn select_index(cumulative_weights: &[f64]) -> usize {
    // TODO: Error Handling
    let w_sum = cumulative_weights.last().unwrap(); 
    let r: f64 = thread_rng().gen_range(0.0, *w_sum);
    cumulative_weights.iter().rposition(|&w| w < r).unwrap()
}


pub fn read_file(filename: &String) -> String {

    let mut file = File::open(filename).unwrap_or_else(|err| {
        eprintln!("Problem opening file. {:?}\n error: {}\n ", filename, err);
        process::exit(1)
    });

    let mut contents = String::new();

    file.read_to_string(&mut contents).unwrap_or_else(|err| { 
        eprintln!("Problem reading file.\n error: {}", err); 
        process::exit(1)
    });

    contents
}


pub fn parse_specs(contents: &String) -> (usize, usize, usize, usize, f64, f64) { 
    // TODO: Error handing unwrapping + Expected number of arguments + Expected type and range of arguments
    let v: Vec<String> = contents.split(',')
                               .map(|val| val.trim().to_string())
                               .collect();

    let debug_level: usize = v[0].parse().unwrap_or_else( |err| {
        eprintln!("debug_level = {} can't be parsed as integer. \n error: {}\n ", v[0], err);
        process::exit(1)
    });

    let skip: usize = v[1].parse().unwrap_or_else( |err| {
        eprintln!("skip = {} can't be parsed as integer. \n error: {}\n ", v[1], err);
        process::exit(1)
    });

    let iterations: usize = v[2].parse().unwrap_or_else( |err| {
        eprintln!("iterations = {} can't be parsed as integer. \n error: {}\n ", v[2], err);
        process::exit(1)
    });

    let population_size: usize = v[3].parse().unwrap_or_else( |err| {
        eprintln!("population_size = {} can't be parsed as integer. \n error: {}\n ", v[3], err);
        process::exit(1)
    });

    let crossover_probability: f64 = v[4].parse().unwrap_or_else( |err| {
        eprintln!("crossover_probability = {} can't be parsed as a float. \n error: {}\n ", v[4], err);
        process::exit(1)
    });

    let mutation_probability: f64 = v[5].parse().unwrap_or_else( |err| {
        eprintln!("mutation_probability = {} can't be parsed as integer. \n error: {}\n ", v[5], err);
        process::exit(1)
    });

    (debug_level, skip, iterations, population_size, crossover_probability, mutation_probability)
}