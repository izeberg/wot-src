package net.wg.portal.data.VO.fullStats
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class PortalEventHeaderVO extends DAAPIDataClass
   {
       
      
      public var title:String = "";
      
      public var subTitle:String = "";
      
      public var description:String = "";
      
      public function PortalEventHeaderVO(param1:Object = null)
      {
         super(param1);
      }
   }
}
