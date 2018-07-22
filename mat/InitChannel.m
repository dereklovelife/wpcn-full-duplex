function [ H ] = InitChannel( k, Nt)

    H1 = normrnd(0, 1, [k, Nt]);
    H2 = normrnd(0, 1, [k, Nt]);
    H = H1 + H2 * 1i;
    
end

