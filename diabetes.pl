my @p1 = (6, 148, 72, 35, 0, 33.6, 0.627, 50);
my @p2 = (1, 85, 66, 29, 0, 26.6, 0.351, 31);

my $sum = 0;
for my $i (0..7) {
    my $diff = $p1[$i] - $p2[$i];
    $sum += $diff * $diff;
}
my $dist = sqrt($sum);

print "Euclidean Distance: $dist\n";
