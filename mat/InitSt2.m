function [ St ] = InitSt2( Hd )

    [n, ~] = size(Hd);
    St = zeros(n, n);
    St(1,1) = 1;

end

