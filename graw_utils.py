class Vers():
    def __init__(self):
        self.mass={}
    def add(self,key,value):
        if key not in  self.mass.keys():
            self.mass[key]=value
    def get_vers(self):
        draw_lines = ''
        draw_lines+='''{{collapse(test)\n'''
        for k,v in self.mass.items():
            draw_lines+=f">{k}\n"
            draw_lines+=f">>>>    {v}\n"
        draw_lines+='''}}'''

        return draw_lines
    

vers = Vers()
vers.add('lic-integrator','awsdasw13')
vers.add('api-lk-license','asdfsdasw13')
print(vers.get_vers())

