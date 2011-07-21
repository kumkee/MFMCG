import pstats
import sys
p = pstats.Stats(sys.argv[1])
p.sort_stats('time')
p.print_stats(.1)
