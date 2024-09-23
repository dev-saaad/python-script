import pandas as pd

class DataFrameWrapper(dict):
    """ a wrapper  around dataframe to manage the overriding/addition of functionalities to DataFrames.
        This is meant to be subclasses by each "excel tables" roughly that we want to use for computations 
    """

    def __init__(self, dataframe, *args, **kwargs):
        # base method need to populate the class with a dataframe
        self.df = dataframe
        self.pandas_callables = [method_name for method_name in dir(self.df) if callable(getattr(self.df, method_name))]
        super(DataFrameWrapper, self).__init__()

    def __getitem__(self, item):
        return self.df[item]

    def __getattr__(self, item):
        """ getattr is only called if attribute lookup on the instance has failed. Thus, if we call .describe() for example on
        our subclass (ProductsDescription, etc.), then the lookup will fail undert __getattribute__(). Then this method
        is called. Here, we check if the item requested (attribute, or method call) is part of what is offered by the
        Dataframe. If so, we return that. If not, we just return the default implementation for __getattr__(). """
        if item in self.pandas_callables:
            # this is a dataframe method call - forward to the dataframe & return that
            return object.__getattribute__(self.df, item)
        else:
            try:                                                # try to return our own attribute, if any
                
                return object.__getattribute__(self, item)
            except AttributeError as ex:
                # likely a panda attribute. IF not, then it's a genuine attribute error, so we don't catch it and let it raise another exception
                try:
                    return object.__getattribute__(self.df, item)
                except Exception as ex:
                    # Try __getitem__, don't catch the error, and let __getitem__ raise an error if it doesn't find it
                        return self.__getitem__(item)

class DataTable(DataFrameWrapper):
    """ Roughly corresponds to an Excel range that has calculated columns, e.g. tables Revenus, Actifs, etc. """

    def __init__(self, dataframe,  *args, **kwargs):
        super().__init__(dataframe)
        # those should match any names defined in the Excel Workbook
        self.calculated_columns = []

        # for outputs - those are the columns we want to include in our outputs. Expects a list of strings for column names
        self.output_cols = []

    def compute_tables(self):
        """ computes the columns for this project. We may want to parametize the actual formula and store them elsewhere,
            but for now it is probably OK to just define them directly in this method.
        """
        raise NotImplemented("Subclasses should implement their own computations here")

    def to_json(self, *args, **kwargs):
        """ ouputs the sheet's dataframe to json.
        :returns: a json-formatted string as per json.dumps(...)
        The implementation is panda's .to_json(), so the same args/kwargs can be passed along.
        """
        # WARNING: using super() here doesn't work. See SO #70979719.
        return DataFrameWrapper.__getattr__(self, "to_json")(*args, **kwargs)

    def to_excel(self, writer, *args, **kwargs):
        """ ouputs the sheet's dataframe to json.
        :returns: a json-formatted string as per json.dumps(...)

        The implementation is panda's .to_excel(), so the same args/kwargs can be passed along.
        """
        # WARNING: using super() here doesn't work. See SO #70979719.
        return DataFrameWrapper.__getattr__(self, "to_excel")(writer, columns=self.output_cols,index=False , *args, **kwargs)

class ProductDescriptionsMacroFile(DataFrameWrapper):
    def __init__(self, dataframe, *arg, **kwargs):
        super().__init__(dataframe, *arg, **kwargs)
        
    @property
    def info(self):
        """ returns the table for info from user input """
        df = pd.DataFrame(self.df.loc[:, "input_key":"input_value"])
        df.index = self.df.loc[:, "input_key"]
        df.input_value = df['input_value'].fillna(0)
        return df.input_value
    
    ####################################################################################################################
    # accessors methods - fee free to define @properties as needed for clean code/syntax
    ####################################################################################################################
