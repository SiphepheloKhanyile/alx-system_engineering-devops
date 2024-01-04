#!/usr/bin/env ruby
#puts ARGV[0].scan(/\b(?!hbon\b)(hbn|hbtn|hbttn|hbtttn|hbttttn)\b/).join
#puts ARGV[0].scan(/\b(?!hbon\b)\w*/).join
puts ARGV[0].scan(/\b(?!hbon\b)(hb(n|t{1,4}))n{1}?/).join
