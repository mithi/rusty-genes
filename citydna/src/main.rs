extern crate citydna;
extern crate rand;

use citydna::Simulation;
use citydna::city;

fn main() {

    let iterations: usize = 1000;
    let population_size: usize = 100; 
    let crossover_probability = 0.6;
    let mutation_probability = 0.001; 

    let cities = city::test_cities(); // vec of 9 cities

    let mut sim = Simulation::new(
        iterations,
        crossover_probability, 
        mutation_probability, 
        population_size,
        cities);

    sim.run(2);
}

