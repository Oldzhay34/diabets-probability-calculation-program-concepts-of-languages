package main

import (
	"fmt"
	"math"
)

func main() {
	p1 := []float64{6, 148, 72, 35, 0, 33.6, 0.627, 50}
	p2 := []float64{1, 85, 66, 29, 0, 26.6, 0.351, 31}

	sum := 0.0
	for i := 0; i < 8; i++ {
		diff := p1[i] - p2[i]
		sum += diff * diff
	}
	dist := math.Sqrt(sum)

	fmt.Println("Euclidean Distance:", dist)
}
