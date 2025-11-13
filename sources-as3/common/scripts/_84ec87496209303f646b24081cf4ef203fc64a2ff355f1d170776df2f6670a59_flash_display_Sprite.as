package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _84ec87496209303f646b24081cf4ef203fc64a2ff355f1d170776df2f6670a59_flash_display_Sprite extends Sprite
   {
       
      
      public function _84ec87496209303f646b24081cf4ef203fc64a2ff355f1d170776df2f6670a59_flash_display_Sprite()
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
