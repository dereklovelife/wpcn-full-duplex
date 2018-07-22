function [ St, th ] = findSt( t, Sr, Hu, Hd, Hsi )

    [k, n] = size(Hd);
    cvx_begin sdp quiet
        variable St(n,n) hermitian semidefinite;
		expression throughput(k);
		for i = 1:k
			throughput(i) = t(i + 1) * log(1 + real(trace(Hd(i,:)' * Hd(i,:) * St)) * real(trace(Hu(i,:)' * Hu(i,:) * Sr)) * sum(t(1:i))/t(i+1));
		end
		maximize(sum(throughput));
		St >= 0;
        trace(St) <= 1;
		trace(Hsi' * Sr * Hsi * St) == 0;
    cvx_end
    th = throughput;
    

end

