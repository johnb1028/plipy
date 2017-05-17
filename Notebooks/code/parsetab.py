
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '7D75FCEF3A507FDC305A63CDC13F494B'
    
_lr_action_items = {'$end':([0,1,2,3,4,7,8,33,34,35,46,54,55,56,],[-26,0,-1,-26,-3,-2,-4,-12,-13,-7,-11,-8,-9,-10,]),'PRINT':([0,3,4,5,8,16,33,34,35,46,54,55,56,],[-26,-26,-6,9,-4,-5,-12,-13,-7,-11,-8,-9,-10,]),'STORE':([0,3,4,5,8,16,33,34,35,46,54,55,56,],[-26,-26,-6,10,-4,-5,-12,-13,-7,-11,-8,-9,-10,]),'JUMPT':([0,3,4,5,8,16,33,34,35,46,54,55,56,],[-26,-26,-6,11,-4,-5,-12,-13,-7,-11,-8,-9,-10,]),'JUMPF':([0,3,4,5,8,16,33,34,35,46,54,55,56,],[-26,-26,-6,12,-4,-5,-12,-13,-7,-11,-8,-9,-10,]),'JUMP':([0,3,4,5,8,16,33,34,35,46,54,55,56,],[-26,-26,-6,13,-4,-5,-12,-13,-7,-11,-8,-9,-10,]),'STOP':([0,3,4,5,8,16,33,34,35,46,54,55,56,],[-26,-26,-6,14,-4,-5,-12,-13,-7,-11,-8,-9,-10,]),'NOOP':([0,3,4,5,8,16,33,34,35,46,54,55,56,],[-26,-26,-6,15,-4,-5,-12,-13,-7,-11,-8,-9,-10,]),'NAME':([0,3,8,9,10,11,12,13,18,19,20,21,22,23,24,25,26,27,28,29,30,33,34,35,36,37,38,39,40,41,46,47,48,49,50,51,52,53,54,55,56,],[6,6,-4,27,28,27,27,32,27,27,27,27,27,27,27,-22,-23,-25,27,32,32,-12,-13,-7,27,27,27,27,27,27,-11,-14,-15,-17,-18,-19,-20,-21,-8,-9,-10,]),':':([6,],[16,]),'+':([9,11,12,18,19,20,21,22,23,24,25,26,27,28,36,37,38,39,40,41,47,48,49,50,51,52,53,],[18,18,18,18,18,18,18,18,18,18,-22,-23,-25,18,18,18,18,18,18,18,-14,-15,-17,-18,-19,-20,-21,]),'-':([9,11,12,18,19,20,21,22,23,24,25,26,27,28,36,37,38,39,40,41,47,48,49,50,51,52,53,],[19,19,19,19,19,19,19,19,19,19,-22,-23,-25,19,19,19,19,19,19,19,-14,-15,-17,-18,-19,-20,-21,]),'*':([9,11,12,18,19,20,21,22,23,24,25,26,27,28,36,37,38,39,40,41,47,48,49,50,51,52,53,],[20,20,20,20,20,20,20,20,20,20,-22,-23,-25,20,20,20,20,20,20,20,-14,-15,-17,-18,-19,-20,-21,]),'/':([9,11,12,18,19,20,21,22,23,24,25,26,27,28,36,37,38,39,40,41,47,48,49,50,51,52,53,],[21,21,21,21,21,21,21,21,21,21,-22,-23,-25,21,21,21,21,21,21,21,-14,-15,-17,-18,-19,-20,-21,]),'EQ':([9,11,12,18,19,20,21,22,23,24,25,26,27,28,36,37,38,39,40,41,47,48,49,50,51,52,53,],[22,22,22,22,22,22,22,22,22,22,-22,-23,-25,22,22,22,22,22,22,22,-14,-15,-17,-18,-19,-20,-21,]),'LE':([9,11,12,18,19,20,21,22,23,24,25,26,27,28,36,37,38,39,40,41,47,48,49,50,51,52,53,],[23,23,23,23,23,23,23,23,23,23,-22,-23,-25,23,23,23,23,23,23,23,-14,-15,-17,-18,-19,-20,-21,]),'(':([9,11,12,18,19,20,21,22,23,24,25,26,27,28,36,37,38,39,40,41,47,48,49,50,51,52,53,],[24,24,24,24,24,24,24,24,24,24,-22,-23,-25,24,24,24,24,24,24,24,-14,-15,-17,-18,-19,-20,-21,]),'NUMBER':([9,11,12,18,19,20,21,22,23,24,25,26,27,28,36,37,38,39,40,41,47,48,49,50,51,52,53,],[26,26,26,26,26,26,26,26,26,26,-22,-23,-25,26,26,26,26,26,26,26,-14,-15,-17,-18,-19,-20,-21,]),';':([14,15,17,25,26,27,31,32,37,43,44,45,47,48,49,50,51,52,53,],[33,34,35,-22,-23,-25,46,-24,-16,54,55,56,-14,-15,-17,-18,-19,-20,-21,]),')':([25,26,27,37,42,47,48,49,50,51,52,53,],[-22,-23,-25,-16,53,-14,-15,-17,-18,-19,-20,-21,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'instr_list':([0,3,],[2,7,]),'labeled_instr':([0,3,],[3,3,]),'empty':([0,3,],[4,4,]),'label_def':([0,3,],[5,5,]),'instr':([5,],[8,]),'exp':([9,11,12,18,19,20,21,22,23,24,28,36,37,38,39,40,41,],[17,29,30,36,37,38,39,40,41,42,43,47,48,49,50,51,52,]),'var':([9,11,12,18,19,20,21,22,23,24,28,36,37,38,39,40,41,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'label':([13,29,30,],[31,44,45,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> instr_list','prog',1,'p_grammar','exp1bytecode_gram.py',6),
  ('instr_list -> labeled_instr instr_list','instr_list',2,'p_grammar','exp1bytecode_gram.py',8),
  ('instr_list -> empty','instr_list',1,'p_grammar','exp1bytecode_gram.py',9),
  ('labeled_instr -> label_def instr','labeled_instr',2,'p_grammar','exp1bytecode_gram.py',11),
  ('label_def -> NAME :','label_def',2,'p_grammar','exp1bytecode_gram.py',13),
  ('label_def -> empty','label_def',1,'p_grammar','exp1bytecode_gram.py',14),
  ('instr -> PRINT exp ;','instr',3,'p_grammar','exp1bytecode_gram.py',16),
  ('instr -> STORE NAME exp ;','instr',4,'p_grammar','exp1bytecode_gram.py',17),
  ('instr -> JUMPT exp label ;','instr',4,'p_grammar','exp1bytecode_gram.py',18),
  ('instr -> JUMPF exp label ;','instr',4,'p_grammar','exp1bytecode_gram.py',19),
  ('instr -> JUMP label ;','instr',3,'p_grammar','exp1bytecode_gram.py',20),
  ('instr -> STOP ;','instr',2,'p_grammar','exp1bytecode_gram.py',21),
  ('instr -> NOOP ;','instr',2,'p_grammar','exp1bytecode_gram.py',22),
  ('exp -> + exp exp','exp',3,'p_grammar','exp1bytecode_gram.py',24),
  ('exp -> - exp exp','exp',3,'p_grammar','exp1bytecode_gram.py',25),
  ('exp -> - exp','exp',2,'p_grammar','exp1bytecode_gram.py',26),
  ('exp -> * exp exp','exp',3,'p_grammar','exp1bytecode_gram.py',27),
  ('exp -> / exp exp','exp',3,'p_grammar','exp1bytecode_gram.py',28),
  ('exp -> EQ exp exp','exp',3,'p_grammar','exp1bytecode_gram.py',29),
  ('exp -> LE exp exp','exp',3,'p_grammar','exp1bytecode_gram.py',30),
  ('exp -> ( exp )','exp',3,'p_grammar','exp1bytecode_gram.py',31),
  ('exp -> var','exp',1,'p_grammar','exp1bytecode_gram.py',32),
  ('exp -> NUMBER','exp',1,'p_grammar','exp1bytecode_gram.py',33),
  ('label -> NAME','label',1,'p_grammar','exp1bytecode_gram.py',35),
  ('var -> NAME','var',1,'p_grammar','exp1bytecode_gram.py',36),
  ('empty -> <empty>','empty',0,'p_empty','exp1bytecode_gram.py',41),
]
