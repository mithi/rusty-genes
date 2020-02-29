## SAMPLE CODE 1
```rust

extern crate citydna;
use citydna::examples;

//use citydna::{City, Simulation};

fn main() {
    //examples::example_one();
    //examples::example_two();

    let c1 = City::new(0, 1.0, 3.0);
    let c2 = City::new(1, 1.0, 2.0);
    let c3 = City::new(2, 1.0, 1.0);
    let cities = vec![c1, c2, c3];

    let iterations: usize = 20;
    let population_size: usize = 10; 
    let crossover_probability = 0.5;
    let mutation_probability = 0.0; 
 
    let mut sim = Simulation::new(
        iterations,
        crossover_probability, 
        mutation_probability, 
        population_size,
        cities
    );

    sim.run(2, 1); // specify debug level = 2, skip = 1
    // skip is unused here since debug level is 2
}

```
### OUTPUT of SAMPLE CODE 1
```bash 
 --------------- 
 STATS 
 --------------- 

BEST TRAVEL PATH: [0, 1, 2]
Fitness Score: 0.5 
0 mutations out of 200 individuals produced
112 cross-overs out of 200 individuals produced

 --------------- 
 SPECS 
 --------------- 

iterations: 20
crossover_probability: 0.5
mutation_probability: 0.0
population_size: 10
number_of_cities: 3

 Cities: 
City { id: 0, x: 1.0, y: 3.0 }
City { id: 1, x: 1.0, y: 2.0 }
City { id: 2, x: 1.0, y: 1.0 }

 --------------- 
 END 
 --------------- 
```
