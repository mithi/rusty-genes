extern crate rand;

use rand::{thread_rng, Rng};

pub mod examples; 
pub mod city;
pub mod helper;
mod individual;
mod simulation;

pub use city::City;
pub use individual::Individual;
pub use simulation::Simulation;

pub fn random_dna(n: usize) -> Vec<usize> {
    let mut v:Vec<usize> = (0..n).collect();
    thread_rng().shuffle(&mut v);
    v
}

pub fn select_parents<'a>(w: &[f64], individuals: &'a [Individual]) -> (&'a Individual, &'a Individual) {
    let mom_index = helper::select_index(w);
    let dad_index = helper::select_index(w);  
    (&individuals[mom_index], &individuals[dad_index])
}

// max_by_key: Ord not implemented for f64
// population.iter().max_by_key(|i| i.fitness).unwrap().clone()
pub fn find_fittest(population: &[Individual]) -> Individual {

    let mut best_individual = &population[0];
    
    for individual in population {
        if best_individual.fitness > individual.fitness {
            best_individual = individual;
        }
    }
    best_individual.clone()
}

pub fn get_cumulative_weights(individuals: &[Individual]) -> Vec<f64> {

    let mut running_sum = 0.0;
    let mut cumulative_weights = vec![running_sum];

    for i in individuals {
        running_sum += i.fitness;
        cumulative_weights.push(running_sum);
    }
    cumulative_weights
}

pub fn random_population(population_size: usize, cities: &[City]) -> Vec<Individual> {

    let number_of_cities = cities.len();
    let mut individuals:Vec<Individual> = Vec::new();
    
    for _ in 0..population_size {
        let dna = random_dna(number_of_cities);
        let indiv = Individual::new(dna, &cities);
        individuals.push(indiv);
    } 
    individuals
}

/*

-----------------------------
ALTERNATIVE SELECT INDEX FUNCTION
-----------------------------

fn select_index(weights: &[f64]) -> usize {
    let w_sum = weights.last().unwrap();
    let mut i = weights.len() - 2;
    let r: f64 = thread_rng().gen_range(0.0, *w_sum);
    while weights[i] > r { i -= 1 }
    i
}

*/