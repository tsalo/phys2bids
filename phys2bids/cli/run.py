# -*- coding: utf-8 -*-
"""
Parser for phys2bids
"""

import argparse

from phys2bids import __version__


def _get_parser():
    """
    Parses command line inputs for this function

    Returns
    -------
    parser.parse_args() : argparse dict

    Notes
    -----
    # Argument parser follow template provided by RalphyZ.
    # https://stackoverflow.com/a/43456577
    """
    parser = argparse.ArgumentParser()
    optional = parser._action_groups.pop()
    required = parser.add_argument_group('Required Argument:')
    required.add_argument('-in', '--input-file',
                          dest='filename',
                          type=str,
                          help='The name of the file containing physiological data, with or '
                               'without extension.',
                          required=True)
    optional.add_argument('-info', '--info',
                          dest='info',
                          action='store_true',
                          help='Only output info about the file, don\'t process. '
                               'Default is to process.',
                          default=False)
    optional.add_argument('-indir', '--input-dir',
                          dest='indir',
                          type=str,
                          help='Folder containing input. '
                               'Default is current folder.',
                          default='.')
    optional.add_argument('-outdir', '--output-dir',
                          dest='outdir',
                          type=str,
                          help='Folder where output should be placed. '
                               'Default is current folder. '
                               'If \"-heur\" is used, it\'ll become '
                               'the site folder. Requires \"-sub\". '
                               'Optional to specify \"-ses\".',
                          default='.')
    optional.add_argument('-heur', '--heuristic',
                          dest='heur_file',
                          type=str,
                          help='File containing heuristic, with or without '
                               'extension. This file is needed in order to '
                               'convert your input file to BIDS format! '
                               'If no path is specified, it assumes the file is '
                               'in the current folder. Edit the heur_ex.py file in '
                               'heuristics folder.',
                          default=None)
    # optional.add_argument('-hdir', '--heur-dir',
    #                       dest='heurdir',
    #                       type=str,
    #                       help='Folder containing heuristic file.',
    #                       default='.')
    optional.add_argument('-sub', '--subject',
                          dest='sub',
                          type=str,
                          help='Specify alongside \"-heur\". Code of '
                               'subject to process.',
                          default=None)
    optional.add_argument('-ses', '--session',
                          dest='ses',
                          type=str,
                          help='Specify alongside \"-heur\". Code of '
                               'session to process.',
                          default=None)
    optional.add_argument('-chtrig', '--channel-trigger',
                          dest='chtrig',
                          type=int,
                          help='The column number of the trigger channel. '
                               'Channel numbering starts with 0. '
                               'Default is 0.',
                          default=0)
    optional.add_argument('-chsel', '--channel-selection',
                          dest='chsel',
                          nargs='*',
                          type=int,
                          help='The column numbers of  the channels to process. '
                               'Default is to process all channels.',
                          default=None)
    optional.add_argument('-ntp', '--numtps',
                          dest='num_timepoints_expected',
                          type=int,
                          help='Number of expected timepoints (TRs). '
                               'Default is 0. Note: the estimation of when the '
                               'neuroimaging acquisition started cannot take place '
                               'with this default.',
                          default=0)
    optional.add_argument('-tr', '--tr',
                          dest='tr',
                          type=float,
                          help='TR of sequence in seconds. '
                               'Default is 0 second.',
                          default=0)
    optional.add_argument('-thr', '--threshold',
                          dest='thr',
                          type=float,
                          help='Threshold to use for trigger detection. '
                               'Default is 2.5.',
                          default=2.5)
    optional.add_argument('-chnames', '--channel-names',
                          dest='ch_name',
                          nargs='*',
                          type=str,
                          help='Column header (for json file output).',
                          default=[])
    optional.add_argument('-chplot', '--channels-plot',
                          dest='chplot',
                          type=str,
                          help='full path to store channels plot ',
                          default='')
    optional.add_argument('-debug', '--debug',
                          dest='debug',
                          action='store_true',
                          help='Only print debugging info to log file. Default is False.',
                          default=False)
    optional.add_argument('-quiet', '--quiet',
                          dest='quiet',
                          action='store_true',
                          help='Only print warnings to log file. Default is False.',
                          default=False)
    optional.add_argument('-v', '--version', action='version',
                          version=('%(prog)s ' + __version__))

    parser._action_groups.append(optional)

    return parser


if __name__ == '__main__':
    raise RuntimeError('phys2bids/cli/run.py should not be run directly;\n'
                       'Please `pip install` phys2bids and use the '
                       '`phys2bids` command')
