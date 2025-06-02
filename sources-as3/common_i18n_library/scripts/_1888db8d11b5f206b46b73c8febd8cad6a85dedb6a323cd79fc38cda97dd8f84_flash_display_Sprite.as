package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _1888db8d11b5f206b46b73c8febd8cad6a85dedb6a323cd79fc38cda97dd8f84_flash_display_Sprite extends Sprite
   {
       
      
      public function _1888db8d11b5f206b46b73c8febd8cad6a85dedb6a323cd79fc38cda97dd8f84_flash_display_Sprite()
      {
         super();
      }
      
      public function allowDomainInRSL(... rest) : void
      {
         Security.allowDomain.apply(null,rest);
      }
      
      public function allowInsecureDomainInRSL(... rest) : void
      {
         Security.allowInsecureDomain.apply(null,rest);
      }
   }
}
