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

  [WebMethod]
  public static dynamic search(string P_DOC_TYPE_CODE, string P_INBOUND_STATUS_COD, string P_STATION_CODE, string P_FREIGHT_CARRIER_CODE)
  {
    OracleConnection _conn;
    List<OracleParameter> _op = new List<OracleParameter>
    {
      new OracleParameter("P_DOC_TYPE_CODE", OracleDbType.Varchar2, P_DOC_TYPE_CODE, ParameterDirection.Input),
      new OracleParameter("P_INBOUND_STATUS_CODE", OracleDbType.Varchar2, P_INBOUND_STATUS_COD, ParameterDirection.Input),
      new OracleParameter("P_STATION_CODE", OracleDbType.Varchar2, P_STATION_CODE, ParameterDirection.Input),
      new OracleParameter("P_FREIGHT_CARRIER_CODE", OracleDbType.Varchar2, P_FREIGHT_CARRIER_CODE, ParameterDirection.Input)
    };
    using (_conn = Common.CreateConnection())
    {
      DataTable result = Common.ExecuteFunction<OracleDataReader>("apps.msi_sti_setup_pkg.get_doc_type_set_data", _op, _conn).ExportToDataTable();
      return JsonConvert.SerializeObject(result);
    }
  }

  [WebMethod]
  public static dynamic insert(string P_DOC_TYPE_CODE, 
                               string P_INBOUND_STATUS_COD, 
                               string P_STATION_CODE, 
                               string P_FREIGHT_CARRIER_CODE,
                               string P_REQUIRED,
                               string P_ALLOW_FILE_TYPE)
  {
    OracleConnection _conn;
    List<OracleParameter> _op = new List<OracleParameter>
      {
        new OracleParameter("P_DOC_TYPE_CODE", OracleDbType.Varchar2, P_DOC_TYPE_CODE, ParameterDirection.Input),
        new OracleParameter("P_INBOUND_STATUS_CODE", OracleDbType.Varchar2, P_INBOUND_STATUS_COD, ParameterDirection.Input),
        new OracleParameter("P_STATION", OracleDbType.Varchar2, P_STATION_CODE, ParameterDirection.Input),
        new OracleParameter("P_FREIGHT_CARRIER", OracleDbType.Varchar2, P_FREIGHT_CARRIER_CODE, ParameterDirection.Input),
        new OracleParameter("P_REQUIRED", OracleDbType.Varchar2, P_REQUIRED, ParameterDirection.Input),
        new OracleParameter("P_ALLOW_FILE_TYPE", OracleDbType.Varchar2, P_ALLOW_FILE_TYPE, ParameterDirection.Input),
        new OracleParameter("P_USER_ID", OracleDbType.Varchar2, Authority.GetUserInfomation(UserProperty.EmployeeNumber), ParameterDirection.Input),
        new OracleParameter("P_ERROR_MESSAGE", OracleDbType.Varchar2, ParameterDirection.Output)
      };

    using (_conn = Common.CreateConnection())
    {
      OracleTransaction trans = _conn.BeginTransaction();
      try
      {
        OracleDataReader result = Common.ExecuteProcedure<OracleDataReader>("apps.msi_sti_setup_pkg.create_doc_type_set", _op, _conn);
        var data = new
        {
          error = result.ExportToDataTable(),
        };
        trans.Commit();
        return data;
      }
      catch (OracleException ex)
      {
        trans.Rollback();
        var data = new
        {
          error = $"新增失敗!<br>{ex.ErrorCode}: {ex.Message}"
        };
        return data;
      }

    }
  }

  [WebMethod]
  public static dynamic update()
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

  [WebMethod]
  public static dynamic delete()
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

  [WebMethod]
  public static dynamic ajax_test(int? id, Boolean is_test, string cmd = "")
  {
    var result = new { id = id.Value, cmd = cmd, is_test = is_test };
    return result;
  }

}