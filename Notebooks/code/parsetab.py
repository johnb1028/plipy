
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftANDORleftEQLEleftPLUSMINUSleftTIMESDIVIDErightUMINUSNOTPLUS MINUS TIMES DIVIDE EQ LE AND OR NOT INTEGER ID STRING INPUT PRINT END IF THEN ELSE ENDIF WHILE ENDWHILE FOR TO STEP NEXT\n    prog : stmt_list\n    \n    stmt_list : stmt stmt_list\n              | stmt\n\n    stmt : ID '=' exp\n         | INPUT opt_string ID\n         | PRINT value value_list\n         | END\n         | IF exp THEN stmt_list opt_else ENDIF\n         | WHILE exp stmt_list ENDWHILE\n         | FOR ID '=' exp TO exp opt_step stmt_list NEXT ID\n    \n    opt_string : STRING ','\n               | empty\n               \n    value_list : ',' value value_list\n               | empty\n               \n    opt_else : ELSE stmt_list\n             | empty\n             \n    opt_step : STEP exp\n             | empty\n\n    exp : exp PLUS exp\n        | exp MINUS exp\n        | exp TIMES exp\n        | exp DIVIDE exp\n        | exp EQ exp\n        | exp LE exp\n        | exp AND exp\n        | exp OR exp\n        | INTEGER\n        | ID\n        | '(' exp ')'\n        | MINUS exp %prec UMINUS\n        | NOT exp\n\n    value : ID\n          | INTEGER\n          | STRING\n    empty :"
    
_lr_action_items = {'ID':([0,3,5,6,7,8,9,10,12,13,15,16,17,18,19,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,47,48,50,51,52,53,54,55,56,57,58,59,61,63,65,66,68,69,70,71,73,74,75,],[4,4,-35,17,-7,23,23,27,23,29,-12,-35,-32,-33,-34,23,-27,-28,23,23,4,-4,-5,-11,-6,17,-14,4,23,23,23,23,23,23,23,23,-30,-31,23,-35,-19,-20,-21,-22,-23,-24,-25,-26,-29,-9,-13,4,23,-8,-35,4,23,-18,-17,75,-10,]),'INPUT':([0,3,7,16,17,18,19,22,23,26,28,29,31,33,34,43,45,48,50,51,52,53,54,55,56,57,58,59,61,63,66,68,69,71,73,75,],[5,5,-7,-35,-32,-33,-34,-27,-28,5,-4,-5,-6,-14,5,-30,-31,-35,-19,-20,-21,-22,-23,-24,-25,-26,-29,-9,-13,5,-8,-35,5,-18,-17,-10,]),'PRINT':([0,3,7,16,17,18,19,22,23,26,28,29,31,33,34,43,45,48,50,51,52,53,54,55,56,57,58,59,61,63,66,68,69,71,73,75,],[6,6,-7,-35,-32,-33,-34,-27,-28,6,-4,-5,-6,-14,6,-30,-31,-35,-19,-20,-21,-22,-23,-24,-25,-26,-29,-9,-13,6,-8,-35,6,-18,-17,-10,]),'END':([0,3,7,16,17,18,19,22,23,26,28,29,31,33,34,43,45,48,50,51,52,53,54,55,56,57,58,59,61,63,66,68,69,71,73,75,],[7,7,-7,-35,-32,-33,-34,-27,-28,7,-4,-5,-6,-14,7,-30,-31,-35,-19,-20,-21,-22,-23,-24,-25,-26,-29,-9,-13,7,-8,-35,7,-18,-17,-10,]),'IF':([0,3,7,16,17,18,19,22,23,26,28,29,31,33,34,43,45,48,50,51,52,53,54,55,56,57,58,59,61,63,66,68,69,71,73,75,],[8,8,-7,-35,-32,-33,-34,-27,-28,8,-4,-5,-6,-14,8,-30,-31,-35,-19,-20,-21,-22,-23,-24,-25,-26,-29,-9,-13,8,-8,-35,8,-18,-17,-10,]),'WHILE':([0,3,7,16,17,18,19,22,23,26,28,29,31,33,34,43,45,48,50,51,52,53,54,55,56,57,58,59,61,63,66,68,69,71,73,75,],[9,9,-7,-35,-32,-33,-34,-27,-28,9,-4,-5,-6,-14,9,-30,-31,-35,-19,-20,-21,-22,-23,-24,-25,-26,-29,-9,-13,9,-8,-35,9,-18,-17,-10,]),'FOR':([0,3,7,16,17,18,19,22,23,26,28,29,31,33,34,43,45,48,50,51,52,53,54,55,56,57,58,59,61,63,66,68,69,71,73,75,],[10,10,-7,-35,-32,-33,-34,-27,-28,10,-4,-5,-6,-14,10,-30,-31,-35,-19,-20,-21,-22,-23,-24,-25,-26,-29,-9,-13,10,-8,-35,10,-18,-17,-10,]),'$end':([1,2,3,7,11,16,17,18,19,22,23,28,29,31,33,43,45,48,50,51,52,53,54,55,56,57,58,59,61,66,75,],[0,-1,-3,-7,-2,-35,-32,-33,-34,-27,-28,-4,-5,-6,-14,-30,-31,-35,-19,-20,-21,-22,-23,-24,-25,-26,-29,-9,-13,-8,-10,]),'ENDWHILE':([3,7,11,16,17,18,19,22,23,28,29,31,33,43,45,46,48,50,51,52,53,54,55,56,57,58,59,61,66,75,],[-3,-7,-2,-35,-32,-33,-34,-27,-28,-4,-5,-6,-14,-30,-31,59,-35,-19,-20,-21,-22,-23,-24,-25,-26,-29,-9,-13,-8,-10,]),'ELSE':([3,7,11,16,17,18,19,22,23,28,29,31,33,43,45,48,49,50,51,52,53,54,55,56,57,58,59,61,66,75,],[-3,-7,-2,-35,-32,-33,-34,-27,-28,-4,-5,-6,-14,-30,-31,-35,63,-19,-20,-21,-22,-23,-24,-25,-26,-29,-9,-13,-8,-10,]),'ENDIF':([3,7,11,16,17,18,19,22,23,28,29,31,33,43,45,48,49,50,51,52,53,54,55,56,57,58,59,61,62,64,66,67,75,],[-3,-7,-2,-35,-32,-33,-34,-27,-28,-4,-5,-6,-14,-30,-31,-35,-35,-19,-20,-21,-22,-23,-24,-25,-26,-29,-9,-13,66,-16,-8,-15,-10,]),'NEXT':([3,7,11,16,17,18,19,22,23,28,29,31,33,43,45,48,50,51,52,53,54,55,56,57,58,59,61,66,72,75,],[-3,-7,-2,-35,-32,-33,-34,-27,-28,-4,-5,-6,-14,-30,-31,-35,-19,-20,-21,-22,-23,-24,-25,-26,-29,-9,-13,-8,74,-10,]),'=':([4,27,],[12,47,]),'STRING':([5,6,32,],[14,19,19,]),'INTEGER':([6,8,9,12,21,24,25,32,35,36,37,38,39,40,41,42,47,65,70,],[18,22,22,22,22,22,22,18,22,22,22,22,22,22,22,22,22,22,22,]),'(':([8,9,12,21,24,25,35,36,37,38,39,40,41,42,47,65,70,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'MINUS':([8,9,12,20,21,22,23,24,25,26,28,35,36,37,38,39,40,41,42,43,44,45,47,50,51,52,53,54,55,56,57,58,60,65,68,70,73,],[21,21,21,36,21,-27,-28,21,21,36,36,21,21,21,21,21,21,21,21,-30,36,-31,21,-19,-20,-21,-22,36,36,36,36,-29,36,21,36,21,36,]),'NOT':([8,9,12,21,24,25,35,36,37,38,39,40,41,42,47,65,70,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),',':([14,16,17,18,19,48,],[30,32,-32,-33,-34,32,]),'THEN':([20,22,23,43,45,50,51,52,53,54,55,56,57,58,],[34,-27,-28,-30,-31,-19,-20,-21,-22,-23,-24,-25,-26,-29,]),'PLUS':([20,22,23,26,28,43,44,45,50,51,52,53,54,55,56,57,58,60,68,73,],[35,-27,-28,35,35,-30,35,-31,-19,-20,-21,-22,35,35,35,35,-29,35,35,35,]),'TIMES':([20,22,23,26,28,43,44,45,50,51,52,53,54,55,56,57,58,60,68,73,],[37,-27,-28,37,37,-30,37,-31,37,37,-21,-22,37,37,37,37,-29,37,37,37,]),'DIVIDE':([20,22,23,26,28,43,44,45,50,51,52,53,54,55,56,57,58,60,68,73,],[38,-27,-28,38,38,-30,38,-31,38,38,-21,-22,38,38,38,38,-29,38,38,38,]),'EQ':([20,22,23,26,28,43,44,45,50,51,52,53,54,55,56,57,58,60,68,73,],[39,-27,-28,39,39,-30,39,-31,-19,-20,-21,-22,-23,-24,39,39,-29,39,39,39,]),'LE':([20,22,23,26,28,43,44,45,50,51,52,53,54,55,56,57,58,60,68,73,],[40,-27,-28,40,40,-30,40,-31,-19,-20,-21,-22,-23,-24,40,40,-29,40,40,40,]),'AND':([20,22,23,26,28,43,44,45,50,51,52,53,54,55,56,57,58,60,68,73,],[41,-27,-28,41,41,-30,41,-31,-19,-20,-21,-22,-23,-24,-25,-26,-29,41,41,41,]),'OR':([20,22,23,26,28,43,44,45,50,51,52,53,54,55,56,57,58,60,68,73,],[42,-27,-28,42,42,-30,42,-31,-19,-20,-21,-22,-23,-24,-25,-26,-29,42,42,42,]),')':([22,23,43,44,45,50,51,52,53,54,55,56,57,58,],[-27,-28,-30,58,-31,-19,-20,-21,-22,-23,-24,-25,-26,-29,]),'TO':([22,23,43,45,50,51,52,53,54,55,56,57,58,60,],[-27,-28,-30,-31,-19,-20,-21,-22,-23,-24,-25,-26,-29,65,]),'STEP':([22,23,43,45,50,51,52,53,54,55,56,57,58,68,],[-27,-28,-30,-31,-19,-20,-21,-22,-23,-24,-25,-26,-29,70,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'stmt_list':([0,3,26,34,63,69,],[2,11,46,49,67,72,]),'stmt':([0,3,26,34,63,69,],[3,3,3,3,3,3,]),'opt_string':([5,],[13,]),'empty':([5,16,48,49,68,],[15,33,33,64,71,]),'value':([6,32,],[16,48,]),'exp':([8,9,12,21,24,25,35,36,37,38,39,40,41,42,47,65,70,],[20,26,28,43,44,45,50,51,52,53,54,55,56,57,60,68,73,]),'value_list':([16,48,],[31,61,]),'opt_else':([49,],[62,]),'opt_step':([68,],[69,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> stmt_list','prog',1,'p_grammar','ubasic_gram.py',20),
  ('stmt_list -> stmt stmt_list','stmt_list',2,'p_grammar','ubasic_gram.py',22),
  ('stmt_list -> stmt','stmt_list',1,'p_grammar','ubasic_gram.py',23),
  ('stmt -> ID = exp','stmt',3,'p_grammar','ubasic_gram.py',25),
  ('stmt -> INPUT opt_string ID','stmt',3,'p_grammar','ubasic_gram.py',26),
  ('stmt -> PRINT value value_list','stmt',3,'p_grammar','ubasic_gram.py',27),
  ('stmt -> END','stmt',1,'p_grammar','ubasic_gram.py',28),
  ('stmt -> IF exp THEN stmt_list opt_else ENDIF','stmt',6,'p_grammar','ubasic_gram.py',29),
  ('stmt -> WHILE exp stmt_list ENDWHILE','stmt',4,'p_grammar','ubasic_gram.py',30),
  ('stmt -> FOR ID = exp TO exp opt_step stmt_list NEXT ID','stmt',10,'p_grammar','ubasic_gram.py',31),
  ('opt_string -> STRING ,','opt_string',2,'p_grammar','ubasic_gram.py',33),
  ('opt_string -> empty','opt_string',1,'p_grammar','ubasic_gram.py',34),
  ('value_list -> , value value_list','value_list',3,'p_grammar','ubasic_gram.py',36),
  ('value_list -> empty','value_list',1,'p_grammar','ubasic_gram.py',37),
  ('opt_else -> ELSE stmt_list','opt_else',2,'p_grammar','ubasic_gram.py',39),
  ('opt_else -> empty','opt_else',1,'p_grammar','ubasic_gram.py',40),
  ('opt_step -> STEP exp','opt_step',2,'p_grammar','ubasic_gram.py',42),
  ('opt_step -> empty','opt_step',1,'p_grammar','ubasic_gram.py',43),
  ('exp -> exp PLUS exp','exp',3,'p_grammar','ubasic_gram.py',45),
  ('exp -> exp MINUS exp','exp',3,'p_grammar','ubasic_gram.py',46),
  ('exp -> exp TIMES exp','exp',3,'p_grammar','ubasic_gram.py',47),
  ('exp -> exp DIVIDE exp','exp',3,'p_grammar','ubasic_gram.py',48),
  ('exp -> exp EQ exp','exp',3,'p_grammar','ubasic_gram.py',49),
  ('exp -> exp LE exp','exp',3,'p_grammar','ubasic_gram.py',50),
  ('exp -> exp AND exp','exp',3,'p_grammar','ubasic_gram.py',51),
  ('exp -> exp OR exp','exp',3,'p_grammar','ubasic_gram.py',52),
  ('exp -> INTEGER','exp',1,'p_grammar','ubasic_gram.py',53),
  ('exp -> ID','exp',1,'p_grammar','ubasic_gram.py',54),
  ('exp -> ( exp )','exp',3,'p_grammar','ubasic_gram.py',55),
  ('exp -> MINUS exp','exp',2,'p_grammar','ubasic_gram.py',56),
  ('exp -> NOT exp','exp',2,'p_grammar','ubasic_gram.py',57),
  ('value -> ID','value',1,'p_grammar','ubasic_gram.py',59),
  ('value -> INTEGER','value',1,'p_grammar','ubasic_gram.py',60),
  ('value -> STRING','value',1,'p_grammar','ubasic_gram.py',61),
  ('empty -> <empty>','empty',0,'p_empty','ubasic_gram.py',66),
]