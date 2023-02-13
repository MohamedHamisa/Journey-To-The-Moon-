def journeyToMoon(n, astronaut):
    sizes = [1]*n
    parents = [i for i in range(n)]
    
    def root(a):
        
        while parents[a] != a:
            # update parent to grandparent
            # this will flatten tree, improving performance
            parents[a] = parents[parents[a]]
            a = parents[a]
        return a
        
    def findset(a, b):
        return root(a) == root(b)
    
    def union(a, b):
        ra = root(a)
        rb = root(b)
        
        # keep tree balanced using sizes array
        if sizes[ra] < sizes[rb]:
            parents[ra] = rb
            sizes[rb] += sizes[ra]
        else:
            parents[rb] = ra
            sizes[ra] += sizes[rb]
            
    for astro in astronaut:
        a = astro[0]
        b = astro[1]
        if not findset(a, b):
            union(a, b)
    
    #print(sizes)
    #print(parents)
    
    roots = [p for i,p in enumerate(parents) if i==p]
    
    #print(roots)
    
    # n choose 2 - sum(country_i choose 2) =>
    # n*n/2 - n/2 - sum(country_i*county_i)/2 + sum(country_i)/2
    # sum(country_i) = n
    # so reduces to just
    # (n*n - sum(country_i*county_i))/2
    N = n**2
    C = 0
    for r in roots:
        C += sizes[r]**2
    
    return (N - C)//2
