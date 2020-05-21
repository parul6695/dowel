
import dowel
from dowel import logger, tabular

logger.add_output(dowel.StdOutput())
logger.add_output(dowel.CsvOutput('out2.csv'))
logger.add_output(dowel.TensorBoardOutput('tensorboard_logdir'))

logger.log('Starting up...')
for i in range(4):
    logger.push_prefix('itr {} '.format(i))
    logger.log('Running training step')

    tabular.record('itr', i)
    tabular.record('loss', 100.0 / (2 + i))

    # the addition of new data to tabular breaks logging to CSV
    if i >=0:
        
        tabular.record('multiplied_data', i*2)
        if i*2>=1:
            tabular.record('new_multiplied_data', i*4)
            

    logger.log(tabular)

    logger.pop_prefix()
    logger.dump_all()

logger.remove_all()
