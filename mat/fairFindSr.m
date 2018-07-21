function [ Sr, th ] = fairFindSr( t, St, Hu, Hd, Hsi )
%UNTITLED7 Summary of this function goes here
%   Detailed explanation goes here
	%% Hd is complex symetric matrix.
    [k, n] = size(Hu);
	% k: num of UE
	% n: Nr 
    cvx_begin sdp quiet
        %cvx_precision low;
        variable Sr(n,n) hermitian semidefinite;
		expression throughput(k);
		for i = 1:k
			throughput(i) = t(i + 1) * log(1 + real(trace(Hd(i,:)' * Hd(i,:) * St)) * real(trace(Hu(i,:)' * Hu(i,:) * Sr)) * sum(t(1:i))/t(i+1));
		end
		maximize(min(throughput));
		Sr >= 0;
        trace(Sr) <= n;
		trace(Sr * Hsi * St * Hsi') == 0;
    cvx_end
    %cvx_status 
    th = throughput;

end

