function[gamma] = find_gamma_hd(Hu, Hd)
	[k, Nt] = size(Hd);
	[k, Nr] = size(Hu);

	St = ones(Nt,Nt) / Nt;
	pre = -1;
	cur = 0;
	while abs(cur - pre) > 0.00005
		pre = cur;
		cvx_begin sdp quiet
        	%cvx_precision low;
			variable Sr(Nr,Nr) hermitian semidefinite;
			expression throughput(k);
			for i = 1:k
				throughput(i) = real(trace(Hd(i,:)' * Hd(i,:) * St)) * real(trace(Hu(i,:)' * Hu(i,:) * Sr));
			end
			maximize(sum(throughput));
			Sr >= 0;
			trace(Sr) <= Nr;
			%trace(Sr * Hsi * St * Hsi') == 0;
		cvx_end

		cvx_begin sdp quiet
        	%cvx_precision low;
			variable St(Nt,Nt) hermitian semidefinite;
			expression throughput(k);
			for i = 1:k
				throughput(i) = real(trace(Hd(i,:)' * Hd(i,:) * St)) * real(trace(Hu(i,:)' * Hu(i,:) * Sr));
			end
			maximize(sum(throughput));
			St >= 0;
			trace(St) <= 1;
			%trace(Sr * Hsi * St * Hsi') == 0;
		cvx_end
		cur = sum(throughput);
        
	end
	gamma = throughput;

