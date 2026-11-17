import math
import unittest
import research_stats as r

class InvalidInputs(unittest.TestCase):
    def test_nonfinite_observations_do_not_become_zero_p(self):
        for v in (float('nan'), float('inf'), -float('inf'), True):
            with self.subTest(value=v), self.assertRaises(ValueError):
                r.newey_west_t([1,v,3],1)
    def test_invalid_null_mean_and_lags(self):
        for v in (float('nan'), float('inf'), True):
            with self.subTest(value=v), self.assertRaises(ValueError):
                r.newey_west_t([1,2,3],1,mu0=v)
            with self.subTest(lags=v), self.assertRaises(ValueError):
                r.newey_west_t([1,2,3],v)
    def test_extreme_finite_range_fails_explicitly(self):
        for x in ([1e308,1e308],[-1e308,1e308],[-1e200,1e200]):
            with self.subTest(x=x), self.assertRaises(ValueError):r.newey_west_t(x,1)
    def test_valid_constant_zero_and_nonzero(self):
        self.assertEqual(r.newey_west_t([0,0,0],1).p_two_sided,1)
        self.assertEqual(r.newey_west_t([.01,.01,.01],1).p_two_sided,0)
    def test_required_n_domains(self):
        for kwargs in ({'sd':-1},{'sd':float('nan')},{'sd':float('inf')},{'effect':float('nan')},{'effect':float('inf')},{'alpha':0},{'alpha':float('nan')},{'power':1},{'power':float('inf')},{'two_sided':1}):
            args={'effect':.1,'sd':1};args.update(kwargs)
            with self.subTest(args=args),self.assertRaises(ValueError):r.required_n(**args)
    def test_zero_effect_valid_domain_only(self):
        self.assertEqual(r.required_n(0,1),math.inf)
        with self.assertRaises(ValueError):r.required_n(0,-1)

if __name__=='__main__':unittest.main()
