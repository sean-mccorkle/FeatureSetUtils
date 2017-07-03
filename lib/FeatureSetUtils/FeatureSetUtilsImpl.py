# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
import json

from FeatureSetUtils.Utils.FeatureSetBuilder import FeatureSetBuilder
#END_HEADER


class FeatureSetUtils:
    '''
    Module Name:
    FeatureSetUtils

    Module Description:
    A KBase module: FeatureSetUtils
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "1.0.0"
    GIT_URL = "https://github.com/Tianhao-Gu/FeatureSetUtils.git"
    GIT_COMMIT_HASH = "ffcc682f1b6cc1c2084a272916f05b36258ef835"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.config = config
        self.config['SDK_CALLBACK_URL'] = os.environ['SDK_CALLBACK_URL']
        self.config['KB_AUTH_TOKEN'] = os.environ['KB_AUTH_TOKEN']
        #END_CONSTRUCTOR
        pass


    def upload_featureset_from_diff_expr(self, ctx, params):
        """
        upload_featureset_from_diff_expr: create a FeatureSet object from a RNASeqDifferentialExpression object
        :param params: instance of type "UploadFeatureSetFromDiffExprInput"
           (required params: diff_expression_ref: RNASeqDifferetialExpression
           object reference feature_set_name: result FeatureSet object name
           p_cutoff: p value cutoff q_cutoff: q value cutoff fold_scale_type:
           one of ["linear", "log2+1", "log10+1"] fold_change_cutoff: fold
           change cutoff workspace_name: the name of the workspace it gets
           saved to) -> structure: parameter "diff_expression_ref" of type
           "obj_ref" (An X/Y/Z style reference), parameter "feature_set_name"
           of String, parameter "p_cutoff" of Double, parameter "q_cutoff" of
           Double, parameter "fold_scale_type" of String, parameter
           "fold_change_cutoff" of Double, parameter "workspace_name" of
           String
        :returns: instance of type "UploadFeatureSetFromDiffExprResult"
           (result_directory: folder path that holds all files generated by
           upload_featureset_from_diff_expr feature_set_ref: generated
           FeatureSet object reference report_name: report name generated by
           KBaseReport report_ref: report reference generated by KBaseReport)
           -> structure: parameter "result_directory" of String, parameter
           "feature_set_ref" of type "obj_ref" (An X/Y/Z style reference),
           parameter "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN upload_featureset_from_diff_expr
        print '--->\nRunning FeatureSetUtils.upload_featureset_from_diff_expr\nparams:'
        print json.dumps(params, indent=1)

        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        fs_builder = FeatureSetBuilder(self.config)
        returnVal = fs_builder.upload_featureset_from_diff_expr(params)
        #END upload_featureset_from_diff_expr

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method upload_featureset_from_diff_expr return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]