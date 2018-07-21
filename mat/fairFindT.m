function [ t, th] = fairFindT(Sr, St, Hu, Hd, Hsi)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here

    [k, ~] = size(Hu);
    gamma = zeros(1,k);
    for i = 1 : k
        gamma(i) = real(trace((Hd(i,:) * St * Hd(i,:)'))) * real(trace(Hu(i,:) * Sr * Hu(i,:)'));
    end
	t = zeros(size(gamma) + [0, 1]);
	lamb = ones(size(gamma)); %% [1, lamb_1/lamb_2,..., lamb_1/lamb_i]
	tmp = size(t);
	tmp = tmp(2);
	zz = zeros(size(gamma)); %% [z1, z2, ..., zi]
	Rmax = 20;
	Rmin = 0;
	while (Rmax - Rmin > 0.005)
		R = (Rmax + Rmin) / 2;

		z_max = 1000;
		z_min = 0;
		while (z_max - z_min > 0.005)
			z = (z_max + z_min) / 2;
			if((1 + z) * log(1 + z) - z > gamma(1))
				z_max = z;
			else
				z_min = z;
            end
		end
		zz(1) = z;
		t(2) = R / log(1 + z);
		t(1) = z / gamma(1) * t(2);
        th(1) = t(2) * log(1 + z);
		for i = 2 : tmp-1
			right = 0;
			for j = 1 : i - 1
				right = right + gamma(j) / (1 + zz(j)) / lamb(j);  
			end

			lamb_max = 100;
			lamb_min = 0;
			while((lamb_max - lamb_min) > 0.005)
				thisLamb = (lamb_max + lamb_min) / 2;
				thisRight = right * thisLamb;
				z_max = 100000;
				z_min = 0;
				while(z_max - z_min > 0.005)
					z = (z_max + z_min) / 2;
					if(log(1 + z) - z / (1 + z) - gamma(i) / (1 + z) > thisRight)
						z_max = z;
					else
						z_min = z;
					end
				end
				tmpT = sum(t(1:i)) * gamma(i) / z;
				if(tmpT * log(1 + z) > R)
					lamb_min = thisLamb;
				else
					lamb_max = thisLamb;
				end
			end
			t(i + 1) = tmpT; 
			zz(i) = z;
            th(i) = t(i + 1) * log(1 + z);
			lamb(i) = thisLamb;
		end

		if((sum(t) > 1))
			Rmax = R;
		else
			Rmin = R;
        end
    end
    
end

