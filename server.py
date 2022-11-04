import asyncio
import os
import tornado.web
import torch
check =os.path.dirname("/workspace/ProgressiveTransformersSLP/Models/Base_2/150_best.ckpt")
cfg_file=os.path.dirname("/workspace/ProgressiveTransformersSLP/Configs")

use_cuda= True
class MainHandler(tornado.web.RequestHandler):
    def get(self,utterance):
        print(utterance)
        u = str(utterance)
        u = u.replace('_',' ')
        data_to_predict = {"test": u}
        model_ceck=torch.load(check, map_location='cuda' if use_cuda else 'cpu')
        
        for f in data_to_predict:
            
            
        
        self.write(u)


def make_app():
    return tornado.web.Application([
        (r"/metod/([^/]+)", MainHandler),
    ])

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())