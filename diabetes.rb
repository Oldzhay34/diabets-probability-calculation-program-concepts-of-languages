p1 = [6, 148, 72, 35, 0, 33.6, 0.627, 50]
p2 = [1, 85, 66, 29, 0, 26.6, 0.351, 31]
 
sum = 0
for i in 0..7
  diff = p1[i] - p2[i]
  sum += diff * diff
end
dist = Math.sqrt(sum)
 
puts "Euclidean Distance: #{dist}"