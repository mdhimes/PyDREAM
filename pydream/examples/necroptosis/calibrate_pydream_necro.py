'''
Generated by pydream_it
PyDREAM run script for necro.py 
'''
from pydream.core import run_dream
from pysb.simulator import ScipyOdeSimulator
import numpy as np
from pydream.parameters import SampledParam
from pydream.convergence import Gelman_Rubin
from scipy.stats import norm,uniform
from necro import model
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
# np.random.seed(0)

# quit()
# fig, ax = plt.subplots(1, 1)
# r = norm.rvs(size=1000)
# ax.hist(norm.stats(loc=3, scale=4), density=True, histtype='stepfilled', alpha=0.2)
# ax.legend(loc='best', frameon=False)
# plt.show()
# quit()
# DREAM Settings
# Number of chains - should be at least 3.
nchains = 5
# Number of iterations
niterations = 10000

#Initialize PySB solver object for running simulations.  Simulation timespan should match experimental data.
# tspan = np.linspace(0,1440, num=100)
# solver = ScipyOdeSimulator(model, tspan=tspan)
# parameters_idxs = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
# rates_mask = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
# param_values = np.array([p.value for p in model.parameters])
#
# # USER must add commands to import/load any experimental data for use in the likelihood function!
# experiments_avg = np.load()
# experiments_sd = np.load()
# like_data = norm(loc=experiments_avg, scale=experiments_sd)
# # USER must define a likelihood function!
# def likelihood(position):
#     Y=np.copy(position)
#     param_values[rates_mask] = 10 ** Y
#     sim = solver.run(param_values=param_values).all
#     logp_data = np.sum(like_data.logpdf(sim['observable']))
#     if np.isnan(logp_data):
#         logp_data = -np.inf
#     return logp_data

obs_names = ['MLKLa_obs']

# Defining a few helper functions to use
def normalize(trajectories):
    """even though this is not really needed, if the data is already between 1 and 0!"""
    """Rescale a matrix of model trajectories to 0-1"""
    ymin = trajectories.min(0)
    ymax = trajectories.max(0)
    return (trajectories - ymin) / (ymax - ymin)

t = np.array([0., 30,  60,   120,  180, 270,  480,  960, 1440])
data = np.array([0., 0., 0., 0., 0.01, 0.05, 0.5, 0.99, 1.])
solver = ScipyOdeSimulator(model, tspan=t) #, rtol=1e-6, # rtol : float or sequence relative tolerance for solution
                            #atol=1e-6) #atol : float or sequence absolute tolerance for solution

rate_params = model.parameters_rules() # these are only the parameters involved in the rules
param_values = np.array([p.value for p in model.parameters]) # these are all the parameters
rate_mask = np.array([p in rate_params for p in model.parameters])  # this picks the element of intersection

def likelihood(position):
    params_tmp = np.copy(position)  # here you pass the parameter vector; the point of making a copy of it is in order not to modify it
    param_values[rate_mask] = 10 ** params_tmp  # see comment above *
    result = solver.run(param_values=param_values)
    ysim_norm = normalize(result.observables['MLKLa_obs'])
    error = np.sum((data - ysim_norm) ** 2)
    return -error


sampled_params_list = list()
sp_p1f = SampledParam(norm, loc=np.log10(3.304257e-05), scale=3.0)
sampled_params_list.append(sp_p1f)
sp_p1r = SampledParam(norm, loc=np.log10(0.009791216), scale=3.0)
sampled_params_list.append(sp_p1r)
sp_p2f = SampledParam(norm, loc=np.log10(0.006110069), scale=3.0)
sampled_params_list.append(sp_p2f)
sp_p3f = SampledParam(norm, loc=np.log10(4.319219e-05), scale=3.0)
sampled_params_list.append(sp_p3f)
sp_p3r = SampledParam(norm, loc=np.log10(0.004212645), scale=3.0)
sampled_params_list.append(sp_p3r)
sp_p4f = SampledParam(norm, loc=np.log10(1.164332e-05), scale=3.0)
sampled_params_list.append(sp_p4f)
sp_p4r = SampledParam(norm, loc=np.log10(0.02404257), scale=3.0)
sampled_params_list.append(sp_p4r)
sp_p5f = SampledParam(norm, loc=np.log10(3.311086e-05), scale=3.0)
sampled_params_list.append(sp_p5f)
sp_p5r = SampledParam(norm, loc=np.log10(0.04280399), scale=3.0)
sampled_params_list.append(sp_p5r)
sp_p6f = SampledParam(norm, loc=np.log10(2.645815e-05), scale=3.0)
sampled_params_list.append(sp_p6f)
sp_p6r = SampledParam(norm, loc=np.log10(0.01437707), scale=3.0)
sampled_params_list.append(sp_p6r)
sp_p7f = SampledParam(norm, loc=np.log10(0.2303744), scale=3.0)
sampled_params_list.append(sp_p7f)
sp_p8f = SampledParam(norm, loc=np.log10(2.980688e-05), scale=3.0)
sampled_params_list.append(sp_p8f)
sp_p8r = SampledParam(norm, loc=np.log10(0.04879773), scale=3.0)
sampled_params_list.append(sp_p8r)
sp_p9f = SampledParam(norm, loc=np.log10(1.121503e-05), scale=3.0)
sampled_params_list.append(sp_p9f)
sp_p9r = SampledParam(norm, loc=np.log10(0.001866713), scale=3.0)
sampled_params_list.append(sp_p9r)
sp_p10f = SampledParam(norm, loc=np.log10(0.7572178), scale=3.0)
sampled_params_list.append(sp_p10f)
sp_p11f = SampledParam(norm, loc=np.log10(1.591283e-05), scale=3.0)
sampled_params_list.append(sp_p11f)
sp_p11r = SampledParam(norm, loc=np.log10(0.03897146), scale=3.0)
sampled_params_list.append(sp_p11r)
sp_p12f = SampledParam(norm, loc=np.log10(3.076363), scale=3.0)
sampled_params_list.append(sp_p12f)
sp_p13f = SampledParam(norm, loc=np.log10(3.73486), scale=3.0)
sampled_params_list.append(sp_p13f)
sp_p13r = SampledParam(norm, loc=np.log10(3.2162e-06), scale=3.0)
sampled_params_list.append(sp_p13r)
sp_p14f = SampledParam(norm, loc=np.log10(8.78243e-05), scale=3.0)
sampled_params_list.append(sp_p14f)
sp_p14r = SampledParam(norm, loc=np.log10(0.02906341), scale=3.0)
sampled_params_list.append(sp_p14r)
sp_p15f = SampledParam(norm, loc=np.log10(5.663104e-05), scale=3.0)
sampled_params_list.append(sp_p15f)
sp_p15r = SampledParam(norm, loc=np.log10(0.02110469), scale=3.0)
sampled_params_list.append(sp_p15r)
sp_p16f = SampledParam(norm, loc=np.log10(0.1294086), scale=3.0)
sampled_params_list.append(sp_p16f)
sp_p16r = SampledParam(norm, loc=np.log10(0.3127598), scale=3.0)
sampled_params_list.append(sp_p16r)
sp_p17f = SampledParam(norm, loc=np.log10(0.429849), scale=3.0)
sampled_params_list.append(sp_p17f)
sp_p18f = SampledParam(norm, loc=np.log10(2.33291e-06), scale=3.0)
sampled_params_list.append(sp_p18f)
sp_p18r = SampledParam(norm, loc=np.log10(0.007077505), scale=3.0)
sampled_params_list.append(sp_p18r)
sp_p19f = SampledParam(norm, loc=np.log10(0.6294062), scale=3.0)
sampled_params_list.append(sp_p19f)
sp_p20f = SampledParam(norm, loc=np.log10(0.06419313), scale=3.0)
sampled_params_list.append(sp_p20f)
sp_p21f = SampledParam(norm, loc=np.log10(0.0008584654), scale=3.0)
sampled_params_list.append(sp_p21f)
sp_p22f = SampledParam(norm, loc=np.log10(8.160445e-05), scale=3.0)
sampled_params_list.append(sp_p22f)
sp_p22r = SampledParam(norm, loc=np.log10(4.354384e-06), scale=3.0)
sampled_params_list.append(sp_p22r)
sp_p23f = SampledParam(norm, loc=np.log10(4.278903), scale=3.0)
sampled_params_list.append(sp_p23f)

# plt.figure()
# sns.distplot(sp_p1f, fit=norm, kde=False)
# plt.show()
# quit()

converged = False
sampled_params, log_ps = run_dream(parameters=sampled_params_list,
                                   likelihood=likelihood,
                                   niterations=niterations,
                                   nchains=nchains,
                                   multitry=False,
                                   gamma_levels=4,
                                   adapt_gamma=True,
                                   history_thin=1,
                                   model_name='dreamzs_5chain',
                                   verbose=True)

total_iterations = niterations
# Save sampling output (sampled parameter values and their corresponding logps).
for chain in range(len(sampled_params)):
    np.save('dreamzs_5chain_sampled_params_chain2_' + str(chain)+'_'+str(total_iterations), sampled_params[chain])
    np.save('dreamzs_5chain_logps_chain2_' + str(chain)+'_'+str(total_iterations), log_ps[chain])
GR = Gelman_Rubin(sampled_params)
print('At iteration: ',total_iterations,' GR = ',GR)
np.savetxt('dreamzs_5chain_GelmanRubin_iteration2_'+str(total_iterations)+'.txt', GR)
old_samples = sampled_params
if np.any(GR>1.2):
    starts = [sampled_params[chain][-1, :] for chain in range(nchains)]
    while not converged:
        total_iterations += niterations
        sampled_params, log_ps = run_dream(parameters=sampled_params_list,
                                           likelihood=likelihood,
                                           niterations=niterations,
                                           nchains=nchains,
                                           start=starts,
                                           multitry=False,
                                           gamma_levels=4,
                                           adapt_gamma=True,
                                           history_thin=1,
                                           model_name='dreamzs_5chain',
                                           verbose=False,
                                           restart=True)
        for chain in range(len(sampled_params)):
            np.save('dreamzs_5chain_sampled_params_chain2_' + str(chain)+'_'+str(total_iterations), sampled_params[chain])
            np.save('dreamzs_5chain_logps_chain2_' + str(chain)+'_'+str(total_iterations), log_ps[chain])
        old_samples = [np.concatenate((old_samples[chain], sampled_params[chain])) for chain in range(nchains)]
        GR = Gelman_Rubin(old_samples)
        print('At iteration: ',total_iterations,' GR = ',GR)
        np.savetxt('dreamzs_5chain_GelmanRubin_iteration2_' + str(total_iterations)+'.txt', GR)
        if np.all(GR<1.2):
            converged = True
try:
    #Plot output
    import seaborn as sns
    from matplotlib import pyplot as plt
    total_iterations = len(old_samples[0])
    burnin = total_iterations/2
    #samples = np.concatenate((old_samples[0][burnin:, :], old_samples[1][burnin:, :], old_samples[2][burnin:, :],old_samples[3][burnin:, :], old_samples[4][burnin:, :]))
    samples = np.concatenate(tuple([old_samples[i][int(burnin):, :] for i in range(nchains)]))
    ndims = len(sampled_params_list)
    colors = sns.color_palette(n_colors=ndims)
    for dim in range(ndims):
        fig = plt.figure()
        sns.distplot(samples[:, dim], color=colors[dim], norm_hist=True)
    fig.savefig('fig_PyDREAM_dimension2_'+str(dim))
except ImportError:
    pass
