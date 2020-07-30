using System;
using System.Data;
using DevExpress.Web;
using Microstar;
using Aspose.Cells;
using Microstar.Data;
using Oracle.ManagedDataAccess.Client;
using System.Drawing;
using Microstar.Security;
using System.Collections.Generic;
using System.Web.Services;
using System.Web.Script.Services;
using Newtonsoft.Json;

public partial class Logistic_Applications_eTracking_Setup_DocUploadTypeSetup_DocUploadTypeSetup : NoScriptBasePage
{
  protected void Page_Load(object sender, EventArgs e)
  {

  }

  [WebMethod]
  public static dynamic get_options()
  {
    OracleConnection _conn;
    List<OracleParameter> _op = new List<OracleParameter>
      {
        new OracleParameter("p_doc_type_list", OracleDbType.RefCursor, ParameterDirection.Output),
        new OracleParameter("p_inbound_status_list", OracleDbType.RefCursor, ParameterDirection.Output),
        new OracleParameter("p_station_list", OracleDbType.RefCursor, ParameterDirection.Output),
        new OracleParameter("p_freight_carrier_list", OracleDbType.RefCursor, ParameterDirection.Output),
        new OracleParameter("p_file_type_list", OracleDbType.RefCursor, ParameterDirection.Output),
      };

    using (_conn = Common.CreateConnection())
    {
      Dictionary<string, OracleDataReader> result = Common.ExecuteProcedure<Dictionary<string, OracleDataReader>>("apps.msi_sti_setup_pkg.get_init_doc_type_set", _op, _conn);
      var data = new
      {
        p_doc_type_list = result["p_doc_type_list"].ExportToDataTable(),
        p_inbound_status_list = result["p_inbound_status_list"].ExportToDataTable(),
        p_station_list = result["p_station_list"].ExportToDataTable(),
        p_freight_carrier_list = result["p_freight_carrier_list"].ExportToDataTable(),
        p_file_type_list = result["p_file_type_list"].ExportToDataTable()
      };
      return JsonConvert.SerializeObject(data);
    }
  }

}