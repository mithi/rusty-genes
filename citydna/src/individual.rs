use super::City;
use rand::{thread_rng, Rng};
pub const MIN_POSITIVE: f64 = 2.2250738585072014e-308f64;

#[derive(Debug, Clone)]
pub struct Individual {
    pub dna: Vec<usize>,
    pub fitness: f64,
}

impl Individual {

    pub fn new(dna: Vec<usize>, cities: &[City]) -> Self {
        let fitness = fitness(&dna, &cities);
        Individual { dna, fitness }
    }

    pub fn cross_over(&self, other: &Individual, cities: &[City]) -> (Self, Self) {

        let n = self.dna.len();
        let mut rng = thread_rng();
        let start = rng.gen_range(0, n - 1);
        let end = rng.gen_range(start + 1, n);

        let daughter_dna = crossover_dna(&self.dna, &other.dna, start, end);
        let son_dna = crossover_dna(&other.dna, &self.dna, start, end);
        
        let daughter = Individual::new(daughter_dna, cities);
        let son = Individual::new(son_dna, cities);
        
        (daughter, son)
    }

    pub fn mutate(&mut self, cities: &[City]) {
        let i = thread_rng().gen_range(0, self.dna.len() - 1);
        self.dna.swap(i, i + 1);
        self.fitness = fitness(&self.dna, &cities);
    }
}

fn fitness(dna: &[usize], cities: &[City]) -> f64 {
    let d = dna.windows(2)
               .fold(MIN_POSITIVE, |acc, w| acc + cities[w[0]].distance_squared(&cities[w[1]]));
    1.0 / d
}

fn crossover_dna(mom: &[usize], dad: &[usize], start: usize, end: usize) -> Vec<usize> {
    
    let mom_slice = &mom[start..=end];
    let mut child: Vec<usize> = Vec::new();
    
    for i in 0..dad.len() {
        if !mom_slice.contains(&dad[i]) {
            child.push(dad[i]);
        }
    }
    
    let end_slice = &child.split_off(start);
    child.extend_from_slice(mom_slice);
    child.extend_from_slice(end_slice);
    child
}

/* 

-----------------------------
ALTERNATIVE FITNESS FUNCTION
-----------------------------

fn fitness(dna: &[usize], cities: &[City]) -> f64 {
    let length = cities.len() - 1;
    let mut d = MIN_POSITIVE;

    for i in 0..length {
        let (j, k) = (dna[i], dna[i+1]);
        d += cities[j].distance_squared(&cities[k]);
    }
    1.0 / d
}

*/