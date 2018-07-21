function [ St, th ] = findSt( t, Sr, Hu, Hd, Hsi )
%UNTITLED7 Summary of this function goes here
%   Detailed explanation goes here
	%% Hd is complex symetric matrix.
    [k, n] = size(Hd);
	% n: num of UE
	% m: Nt 
    cvx_begin sdp quiet
        %cvx_precision low;
        variable St(n,n) hermitian semidefinite;
        
		expression throughput(k);
		for i = 1:k
			throughput(i) = t(i + 1) * log(1 + real(trace(Hd(i,:)' * Hd(i,:) * St)) * real(trace(Hu(i,:)' * Hu(i,:) * Sr )) * sum(t(1:i)) / t(i+1));
		end
		maximize(sum(throughput));
		St >= 0;
        trace(St) <= 1;
		trace(Hsi' * Sr * Hsi * St) == 0;
    cvx_end
    th = throughput;
    

end

