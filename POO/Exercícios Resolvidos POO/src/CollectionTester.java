import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class CollectionTester {

	public static void main(String[] args) {
		int dim = 5000;

		Collection<Integer> col = new ArrayList<>();
		Map<String, Double> res = checkPerformance(col, dim);
		System.out.println(col.getClass().getSimpleName());
		System.out.println(res);
	}

	private static Map<String, Double> checkPerformance(Collection<Integer> col, final int DIM) {
		double start, stop, delta;
		Map<String, Double> out = new HashMap<>();

		// Add
		start = System.nanoTime(); // clock snapshot before
		for(int i=0; i<DIM; i++ )
			col.add( i );
		stop = System.nanoTime();  // clock snapshot after
		delta = (stop-start)/1e6; // convert to milliseconds
		out.put("add", delta);

		// Search
		start = System.nanoTime(); // clock snapshot before
		for(int i=0; i<DIM; i++ ) {
			int n = (int) (Math.random()*DIM);
			if (!col.contains(n)) 
				System.out.println("Not found???"+n);
		}
		stop = System.nanoTime();  // clock snapshot after
		delta = (stop-start)/1e6; // convert nanoseconds to milliseconds
		out.put("search", delta);

		// Remove
		start = System.nanoTime(); // clock snapshot before
		Iterator<Integer> iterator = col.iterator();
		while (iterator.hasNext()) {
			iterator.next();
			iterator.remove();
		}
		stop = System.nanoTime();  // clock snapshot after
		delta = (stop-start)/1e6; // convert nanoseconds to milliseconds
		out.put("remove", delta);

		return out;
	}
}