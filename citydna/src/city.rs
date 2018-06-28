use rand::{thread_rng, Rng};

#[derive(Debug)]
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

pub fn test_cities() -> Vec<City> {
    /*
                 8* 
        0*    5* 3*
        1*    6*
        2* 4* 7*
       
    */

    let c1 = City::new(0, 1.0, 3.0);
    let c2 = City::new(1, 1.0, 2.0);
    let c3 = City::new(2, 1.0, 1.0);
    let c4 = City::new(3, 4.0, 3.0);
    let c5 = City::new(4, 2.0, 1.0);
    let c6 = City::new(5, 3.0, 3.0);
    let c7 = City::new(6, 3.0, 2.0);
    let c8 = City::new(7, 3.0, 1.0);
    let c9 = City::new(8, 4.0, 4.0);

    vec![c1, c2, c3, c4, c5, c6, c7, c8, c9]
}
