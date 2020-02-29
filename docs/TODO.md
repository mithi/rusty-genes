# TODO FOR KNOWN ISSUES
- Documentation of `debug_level` parameter
- Error-handling of `helper::parse_specs`
- Error-handling of `city::string_to_cities()`
- Error-handling of `helper::select_index()`
- Other `citydna::find_fittest()` function 
- Other `individual::mutate()` and `individual::cross_over()` strategies
- Incorporate early-stopping

# FUTURE FEATURES (TODO)
## 1. RUN EXAMPLE FROM COMMAND LINE
```bash
$ cargo run example 1
$ cargo run example 2
```

## 2. MORE SOPHISTICATED SIMULATION
```bash
$ cargo run simulate ./specification.csv ./cities.csv > output.csv

./output.csv
#, A, SCOREA, [A], B, SCOREB, [B]
1, A, 0.125, 1, 5, 4, 2, 3, B, 0.1, 1, 2, 3, 4, 5 
...
```

## 3. SIMULATION WITH RANDOM CITIES 
```
$ cargo run simulate ./specification.csv ?15 > output.csv
```

## 4. GENERATE CITIES
```
cargo run generate number_of_cities random minimum_x maximum_x minimum_y maximum_y > output_path
cargo run generate number_of_cities circle center_x center_y radius > output_path
cargo run generate number_of_cities cos A W K B > output_path

cargo run generate 15 random 0 100 -20 15 > ./cities.txt
cargo run generate 20 circle 10 20 5 > ./cities.txt
cargo run generate 1 cos 5 0 0 0 > ./cities.txt
note: A * cos(Wt + B) + K 
```
