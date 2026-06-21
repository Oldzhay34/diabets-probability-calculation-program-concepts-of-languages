let p1 = [6, 148, 72, 35, 0, 33.6, 0.627, 50];
let p2 = [1, 85, 66, 29, 0, 26.6, 0.351, 31];

let sum = 0;
for (let i = 0; i < 8; i++) {
    let diff = p1[i] - p2[i];
    sum += diff * diff;
}
let dist = Math.sqrt(sum);

console.log("Euclidean Distance: " + dist);
