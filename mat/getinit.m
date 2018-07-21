function [ th ] = getinit( St,Sr,t, Hd, Hu )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
    th = 0;
    [k, ~] = size(Hu);
    
    for i = 1:k
        th(i) = log(1 + real(trace(Hu(i,:)' * Hu(i,:) * Sr)) * real(trace(Hd(i,:)' * Hd(i,:) * St)) * i);
    end
    th = th / (k + 1);
end

