function swap(a,i,j){
  tmp = a[i];
  a[i] = a[j]; //only swap the values.
  a[j] = tmp;
}

function heapify(a, N){
  var parent_ = N;
	var start = parent_;
  var child_left = 2*root + 1;
  var child_right = 2*root + 2;
  if ((child_left < N) && (a[root] < a[child_left])){
    large_index = child_left;
  }
  if ((child_right < N) && a[large_index] < a[child_right]){
    large_index = child_right;
  }
	while(start >= 0){
		down_heap(a,start,N-1)
		start -= 1;
	}
}

function down_heap(a,root,end){
	var swap_index = root;
	var left_child = 2*root + 1
	var left_child = 2*root + 2
	if ((child_left < n) &&	(a[root] < a[child_left])){
				large_index = child_left;
	}
	if ((child_right < n) && a[large_index] < a[child_right]){
		large_index = child_right;
	}
	if (large_index != root){
		swap(a, large_index, root);
		down_heap(a, large_index, N);
	}
}

function heap_sort(a){
	heapify(a)
	n = a.len-1
	while(n > 0):
		swap(a, 0, n)
		n -= 1
		down_heapify(a,0,n)
}

heap_sort(a)

