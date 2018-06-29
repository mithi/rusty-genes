use rand::{thread_rng, Rng};
use std::str::FromStr;

#[derive(Debug, Clone)]
pub struct City {
    id: usize,
    x: f64,
    y: f64,
}

impl City {

    pub fn new(id: usize, x: f64, y: f64) -> Self {
        City { id, x, y }
    }

    pub fn distance_squared(&self, other: &City) -> f64 {
        let d1 = self.x - other.x;
        let d2 = self.y - other.y;
        d1 * d1 + d2 * d2
    }
}

pub fn string_to_cities(contents: &String) -> Vec<City> {
    //TODO: Error handling: Unwrapping of line + expected # elements 
    let mut cities: Vec<City> = Vec::new();

    for (i, line) in contents.lines().enumerate() {

        let values: Vec<f64> = line.split(',')
                                   .map(|val| f64::from_str(val.trim())
                                   .unwrap())
                                   .collect();
        
        let c = City::new(i, values[1], values[2]);
        cities.push(c);
    }
    cities
}

pub fn random_cities(n: usize, mn: f64, mx: f64) -> Vec<City> {

    let mut rng = thread_rng();
    let mut cities:Vec<City> = Vec::new();

    for i in 0..n {
        let x: f64 = rng.gen_range(mn, mx);
        let y: f64 = rng.gen_range(mn, mx);
        let c = City::new(i, x, y);
        cities.push(c);
    }
    cities
}