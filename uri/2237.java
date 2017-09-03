import java.util.Arrays;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Set;

// 2237 - https://www.urionlinejudge.com.br/judge/en/problems/view/2237


public class Containers {
	
	static class Movement {
		int from, to;
		Movement(int f, int t) {
			this.from = f;
			this.to = t;
		}
	}
	
	static class State implements Comparable<State>{
		int[] data;
		int cost;
		State(int[] data) {
			this.data = data;
		}

		@Override
		public int hashCode() {
			final int prime = 31;
			int result = 1;
			result = prime * result + Arrays.hashCode(data);
			return result;
		}

		@Override
		public boolean equals(Object obj) {
			if (this == obj)
				return true;
			if (obj == null)
				return false;
			if (getClass() != obj.getClass())
				return false;
			State other = (State) obj;
			if (!Arrays.equals(data, other.data))
				return false;
			return true;
		}

		@Override
		public int compareTo(State o) {
			return Integer.compare(this.cost, o.cost);
		}
		
		public State clone() {
			State c = new State(this.data.clone());
			c.cost = this.cost;
			return c;
		}
		
		public int swap(Movement m) {
			int aux = this.data[m.to];
			this.data[m.to] = this.data[m.from];
			this.data[m.from] = aux;
			int cost = this.data[m.to] + this.data[m.from]; 
			return cost;
		}
	}

	public static void main(String[] args) {
		try(Scanner in = new Scanner(System.in)) {
			int[] initial_state_data = new int[8];
			int[] goal_state_data = new int[8];
			for (int i = 0; i < 8; i++) {
				initial_state_data[i] = in.nextInt();
			}
			for (int i = 0; i < 8; i++) {
				goal_state_data[i] = in.nextInt();
			}
			State initial_state = new State(initial_state_data);
			initial_state.cost = 0;
			State goal_state = new State(goal_state_data);
			
			Movement[] movements = { new Movement(0, 1), new Movement(1, 2), new Movement(2, 3),
					new Movement(4, 5), new Movement(5, 6), new Movement(6, 7),
					new Movement(0, 4), new Movement(1, 5), new Movement(2, 6), new Movement(3, 7)};
			
			PriorityQueue<State> q = new PriorityQueue<>();
			q.add(initial_state);
			int minimum_cost = 0;
			Set<State> visited = new HashSet<>(20000);
			while (!q.isEmpty()) {				
				State current_state = q.poll();
				if (current_state.equals(goal_state)) {
					minimum_cost = current_state.cost;
					break;
				}
				if (!visited.contains(current_state)) {
					visited.add(current_state);
					for (Movement m : movements) {
						State new_state = current_state.clone();
						int movement_cost = new_state.swap(m);
						new_state.cost += movement_cost;
						q.add(new_state);
					}
				}
				
			}
			System.out.println(minimum_cost);
		}
	}

}
