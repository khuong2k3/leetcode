struct Solution;

impl Solution {
    pub fn my_atoi(s: String) -> i32 {
        let mut ans = 0;
        let mut s: Vec<_> = s.chars().collect();
        for c in s {
        }

        return ans
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {

        println!("{}", Solution::my_atoi("sdf".into()));
    }
}
