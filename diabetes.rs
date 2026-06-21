fn main() {
    let p1 = [6.0, 148.0, 72.0, 35.0, 0.0, 33.6, 0.627, 50.0];
    let p2 = [1.0, 85.0, 66.0, 29.0, 0.0, 26.6, 0.351, 31.0];

    let mut sum: f64 = 0.0;
    for i in 0..8 {
        let diff = p1[i] - p2[i];
        sum += diff * diff;
    }
    let dist = sum.sqrt();

    println!("Euclidean Distance: {}", dist);
}