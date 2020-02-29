## SAMPLE CODE 2

```rust 

/*

---------------------
                 8* 
        0*    5* 3*
        1*    6*
        2* 4* 7*
---------------------
*/

// -------------------- 
// Generate 9 cities
// --------------------

let c1 = City::new(0, 1.0, 3.0);
let c2 = City::new(1, 1.0, 2.0);
let c3 = City::new(2, 1.0, 1.0);
let c4 = City::new(3, 4.0, 3.0);
let c5 = City::new(4, 2.0, 1.0);
let c6 = City::new(5, 3.0, 3.0);
let c7 = City::new(6, 3.0, 2.0);
let c8 = City::new(7, 3.0, 1.0);
let c9 = City::new(8, 4.0, 4.0);

let cities = vec![c1, c2, c3, c4, c5, c6, c7, c8, c9]

// -------------------- 
// RUN  SIMULATION FOR  `t` ITERATIONS
// --------------------

let mut n = 0;
let t = 200;
let expected_fitness = 0.125;
let solution = vec![
    vec![0, 1, 2, 4, 7, 6, 5, 3, 8], 
    vec![8, 3, 5, 6, 7, 4, 2, 1, 0]];

for i in 0..t {

    let cities = cities.clone();

    let mut sim = Simulation::new(
        1000,
        0.8, 
        0.001, 
        100,
        cities
    );

    sim.run(0, 1);

    if sim.fitness == expected_fitness {
        if sim.dna == solution[0] || sim.dna == solution[1] {
            n += 1;
        }
        println!("{}:{}", i, n);
    }
}

let percent_correct = 100.0 * n as f64 / t as f64;
println!("\n --------------- \n {}% correct of {} simulations \n --------------- \n", percent_correct, t);

```
### OUTPUT OF SAMPLE CODE 2
```bash
0:1
1:2
2:3
3:4
4:5
6:6
9:7
12:8
14:9
15:10
16:11
# --- snip ---
143:113
146:114
148:115
149:116

 --------------- 
 77.33333333333333% correct with 150 simulations 
 --------------- 
```
