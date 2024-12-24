
"""
Write the question summary here
"""
              
test_data_a = """
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj
""".strip()
test_data_b = test_data_a
test_answer_a = 2024
test_answer_b = test_answer_a
              

def _compute(operand_1, operator, operand_2):
  operand_1 = int(operand_1)
  operand_2 = int(operand_2)

  if operator == "AND":
    return operand_1 & operand_2
  elif operator == "OR":
    return operand_1 | operand_2
  elif operator == "XOR":
    return operand_1 ^ operand_2

def solve_a(data):
  answer = 0

  initials, equations = data.split("\n\n")
  wires = {}
  for line in initials.split("\n"):
    wire, value = line.split(": ")
    wires[wire] = value
  
  equations = equations.split("\n")
  for i in range(len(equations)):
    equation, output_wire = equations[i].split(" -> ")
    operand_1, operator, operand_2 = equation.split(" ")
    equations[i] = {
      "operands": (operand_1, operand_2),
      "operator": operator,
      "output": output_wire
    }

  z_length = -1
  while equations:
    equation = equations.pop(0)
    operand_1, operand_2 = equation["operands"]
    if operand_1 in wires and operand_2 in wires:
      wires[equation["output"]] = _compute(wires[operand_1], equation["operator"], wires[operand_2])
      if equation["output"][0] == "z":
        z_length = max(z_length, int(equation["output"][1:]))
    else:
      equations.append(equation)
  
  digit_count = len(str(z_length))
  answer_bits = ""
  for i in range(z_length + 1):
    answer_bits += str(wires[f"z{i:0{digit_count}}"])
  
  answer = int(answer_bits[::-1], 2)
  return answer
              
def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"

               
def solve_b(data):
  answer = 0
  return answer
              
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"

              
if __name__ == "__main__":
  test_a()
  test_b()
