function [ St ] = InitSt( Hd )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
    [~,Nt] = size(Hd);
    cvx_begin sdp quiet
    
    %cvx_precision low;
        variable St(Nt, Nt) hermitian semidefinite;
        maximize(trace(Hd * St * Hd'));
        trace(St) <= 1;
        St >= 0;
    cvx_end

end

