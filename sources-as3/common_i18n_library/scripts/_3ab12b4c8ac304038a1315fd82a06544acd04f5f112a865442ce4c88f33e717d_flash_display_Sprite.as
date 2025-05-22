package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _3ab12b4c8ac304038a1315fd82a06544acd04f5f112a865442ce4c88f33e717d_flash_display_Sprite extends Sprite
   {
       
      
      public function _3ab12b4c8ac304038a1315fd82a06544acd04f5f112a865442ce4c88f33e717d_flash_display_Sprite()
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
