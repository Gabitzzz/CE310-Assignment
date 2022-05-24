for file in sys.argv[2:]:
    if file != probe_file:
        im = cv2.imread (file)
        a + h = histogram (im)
        v = compare (probe, h)
        if v > v_best:
            v_best = v
            f_best = file
print (f_best)