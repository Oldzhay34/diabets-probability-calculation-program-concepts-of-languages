let p1 = [| 6.0; 148.0; 72.0; 35.0; 0.0; 33.6; 0.627; 50.0 |]
let p2 = [| 1.0; 85.0; 66.0; 29.0; 0.0; 26.6; 0.351; 31.0 |]

let mutable sum = 0.0
for i in 0..7 do
    let diff = p1.[i] - p2.[i]
    sum <- sum + diff * diff

let dist = sqrt sum
printfn "Euclidean Distance: %f" dist
