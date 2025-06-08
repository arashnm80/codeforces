use std::collections::HashSet;
use std::io::{self, BufRead};

fn solve_test_case(arr: Vec<i32>) -> i32 {
    let mut count = 1;
    let mut check = HashSet::new();
    let mut biggest_set = HashSet::new();

    for val in arr {
        check.insert(val);

        if biggest_set.is_empty() {
            biggest_set = check.clone();
            check.clear();
            continue;
        }

        if biggest_set.is_subset(&check) {
            count += 1;
            biggest_set = check.clone();
            check.clear();
        }
    }

    count
}

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines().map(|l| l.unwrap());

    let t: usize = lines.next().unwrap().trim().parse().unwrap();

    for _ in 0..t {
        let n: usize = lines.next().unwrap().trim().parse().unwrap();
        let arr: Vec<i32> = lines
            .next()
            .unwrap()
            .split_whitespace()
            .map(|x| x.parse().unwrap())
            .collect();

        let result = solve_test_case(arr);
        println!("{}", result);
    }
}
